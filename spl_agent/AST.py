import os
import ast
from pathlib import Path
from typing import Dict, List, Any
import json


class ASTProcessor:
    """AST处理器 - 专门用于分析Code文件夹中的Python文件"""

    def __init__(self):
        self.analysis_results = {}

    def extract_ast_from_python_file(self, file_path: Path) -> Dict[str, Any]:
        """从Python文件中提取完整的AST结构"""
        print(f"分析文件: {file_path}")

        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        try:
            tree = ast.parse(content)
        except SyntaxError as e:
            print(f"语法错误在文件 {file_path}: {e}")
            return {"error": str(e)}

        file_ast = {
            "file_name": file_path.name,
            "file_path": str(file_path),
            "content_length": len(content),
            "classes": {},
            "global_functions": [],
            "imports": [],
            "global_variables": [],
            "ast_structure": {}
        }

        # 提取导入语句
        file_ast["imports"] = self._extract_imports(tree)

        # 提取全局变量
        file_ast["global_variables"] = self._extract_global_variables(tree, content)

        # 提取类和函数
        file_ast["classes"] = self._extract_classes(tree, content)
        file_ast["global_functions"] = self._extract_global_functions(tree, content)

        # 生成完整的AST结构
        file_ast["ast_structure"] = self._generate_ast_structure(tree)

        return file_ast

    def _extract_imports(self, tree: ast.AST) -> List[Dict]:
        """提取导入语句"""
        imports = []

        for node in tree.body:
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imports.append({
                        "type": "import",
                        "module": alias.name,
                        "alias": alias.asname,
                        "lineno": node.lineno
                    })
            elif isinstance(node, ast.ImportFrom):
                for alias in node.names:
                    imports.append({
                        "type": "from_import",
                        "module": node.module,
                        "name": alias.name,
                        "alias": alias.asname,
                        "level": node.level,
                        "lineno": node.lineno
                    })

        return imports

    def _extract_global_variables(self, tree: ast.AST, content: str) -> List[Dict]:
        """提取全局变量"""
        global_vars = []

        for node in tree.body:
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name):
                        var_code = ast.get_source_segment(content, node)
                        global_vars.append({
                            "name": target.id,
                            "code": var_code,
                            "lineno": node.lineno,
                            "type": "assignment"
                        })
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                var_code = ast.get_source_segment(content, node)
                global_vars.append({
                    "name": node.target.id,
                    "code": var_code,
                    "lineno": node.lineno,
                    "type": "annotated_assignment"
                })

        return global_vars

    def _extract_classes(self, tree: ast.AST, content: str) -> Dict[str, Any]:
        """提取类定义"""
        classes = {}

        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                class_name = node.name
                classes[class_name] = {
                    "name": class_name,
                    "lineno": node.lineno,
                    "bases": [self._get_base_name(base) for base in node.bases],
                    "methods": [],
                    "class_variables": [],
                    "decorators": [self._get_decorator_name(decorator) for decorator in node.decorator_list]
                }

                # 提取类中的方法
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        method_info = self._extract_function_info(item, content)
                        classes[class_name]["methods"].append(method_info)

                    # 提取类变量
                    elif isinstance(item, ast.Assign):
                        for target in item.targets:
                            if isinstance(target, ast.Name):
                                var_code = ast.get_source_segment(content, item)
                                classes[class_name]["class_variables"].append({
                                    "name": target.id,
                                    "code": var_code,
                                    "lineno": item.lineno
                                })

        return classes

    def _extract_global_functions(self, tree: ast.AST, content: str) -> List[Dict]:
        """提取全局函数"""
        global_functions = []

        for node in tree.body:
            if isinstance(node, ast.FunctionDef):
                # 跳过魔术方法（除了__init__）
                if not node.name.startswith('__') or node.name == '__init__':
                    func_info = self._extract_function_info(node, content)
                    global_functions.append(func_info)

        return global_functions

    def _extract_function_info(self, func_node: ast.FunctionDef, content: str) -> Dict[str, Any]:
        """提取函数的详细信息"""
        func_code = ast.get_source_segment(content, func_node)

        # 提取参数信息
        args_info = self._extract_arguments_info(func_node.args)

        # 分析函数体结构
        body_analysis = self._analyze_function_body(func_node.body, content)

        # 生成简化的AST结构，避免复杂的嵌套
        simplified_ast = self._generate_simplified_ast_structure(func_node)

        return {
            "name": func_node.name,
            "code": func_code,
            "lineno": func_node.lineno,
            "args": args_info,
            "decorators": [self._get_decorator_name(decorator) for decorator in func_node.decorator_list],
            "returns": self._get_annotation_name(getattr(func_node, 'returns', None)),
            "body_analysis": body_analysis,
            "ast_structure": simplified_ast  # 使用简化的AST结构
        }

    def _generate_simplified_ast_structure(self, node: ast.AST) -> Dict[str, Any]:
        """生成简化的AST结构，避免深度嵌套"""
        node_type = type(node).__name__
        result = {
            "type": node_type,
            "lineno": getattr(node, 'lineno', None)
        }

        # 只处理关键信息，避免深度递归
        if isinstance(node, ast.FunctionDef):
            result["name"] = node.name
            result["args_count"] = len(node.args.args)
        elif isinstance(node, ast.ClassDef):
            result["name"] = node.name
            result["bases_count"] = len(node.bases)

        return result

    def _get_annotation_name(self, annotation: Any) -> str:
        """获取类型注解的名称"""
        if annotation is None:
            return None
        elif isinstance(annotation, ast.Name):
            return annotation.id
        elif isinstance(annotation, ast.Attribute):
            return ast.unparse(annotation)
        elif isinstance(annotation, ast.Subscript):
            return ast.unparse(annotation)
        else:
            return str(type(annotation).__name__)

    def _extract_arguments_info(self, args: ast.arguments) -> Dict[str, Any]:
        """提取函数参数信息"""
        arguments = {
            "args": [arg.arg for arg in args.args],
            "defaults": len(args.defaults),
            "vararg": args.vararg.arg if args.vararg else None,
            "kwarg": args.kwarg.arg if args.kwarg else None,
            "kwonlyargs": [arg.arg for arg in args.kwonlyargs]
        }

        return arguments

    def _analyze_function_body(self, body: List[ast.AST], content: str) -> Dict[str, Any]:
        """分析函数体结构 - 添加Switch节点分析"""
        analysis = {
            "statements_count": len(body),
            "control_structures": [],
            "loops": [],
            "assignments": [],
            "function_calls": [],
            "switch_cases": []  # 新增：Switch语句分析
        }

        for node in body:
            if isinstance(node, ast.If):
                analysis["control_structures"].append({
                    "type": "if",
                    "lineno": node.lineno,
                    "code": ast.get_source_segment(content, node)
                })
            elif isinstance(node, ast.For):
                analysis["loops"].append({
                    "type": "for",
                    "lineno": node.lineno,
                    "code": ast.get_source_segment(content, node)
                })
            elif isinstance(node, ast.While):
                analysis["loops"].append({
                    "type": "while",
                    "lineno": node.lineno,
                    "code": ast.get_source_segment(content, node)
                })
            elif isinstance(node, ast.Assign):
                analysis["assignments"].append({
                    "type": "assignment",
                    "lineno": node.lineno,
                    "code": ast.get_source_segment(content, node)
                })
            elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
                analysis["function_calls"].append({
                    "type": "function_call",
                    "lineno": node.lineno,
                    "code": ast.get_source_segment(content, node)
                })
            elif isinstance(node, ast.Match):  # Python 3.10+ 的match语句（类似Switch）
                analysis["switch_cases"].append({
                    "type": "match",
                    "lineno": node.lineno,
                    "code": ast.get_source_segment(content, node)
                })

        return analysis

    def _generate_ast_structure(self, node: ast.AST, depth: int = 0) -> Dict[str, Any]:
        """生成AST节点的结构信息 - 修复JSON序列化问题和版本兼容性"""
        if depth > 10:  # 防止无限递归
            return {"type": "max_depth_reached"}

        if not isinstance(node, ast.AST):
            return {"type": "non_ast_node", "value": str(node)}

        node_type = type(node).__name__
        result = {
            "type": node_type,
            "lineno": getattr(node, 'lineno', None),
            "col_offset": getattr(node, 'col_offset', None)
        }

        # 处理特定节点类型的额外信息 - 只提取可序列化的数据
        try:
            if isinstance(node, ast.Name):
                result["id"] = node.id
                result["ctx"] = type(node.ctx).__name__
            elif isinstance(node, ast.Call):
                result["func"] = self._generate_ast_structure(node.func, depth + 1)
                result["args"] = [self._generate_ast_structure(arg, depth + 1) for arg in node.args]
                if node.keywords:
                    result["keywords"] = [{"arg": kw.arg, "value": self._generate_ast_structure(kw.value, depth + 1)}
                                          for kw in node.keywords]
            elif isinstance(node, ast.Assign):
                result["targets"] = [self._generate_ast_structure(target, depth + 1) for target in node.targets]
                result["value"] = self._generate_ast_structure(node.value, depth + 1)
            elif isinstance(node, ast.FunctionDef):
                result["name"] = node.name
                result["args"] = self._generate_ast_structure(node.args, depth + 1)
                result["decorator_list"] = [self._generate_ast_structure(decorator, depth + 1)
                                            for decorator in node.decorator_list]
            elif isinstance(node, ast.ClassDef):
                result["name"] = node.name
                result["bases"] = [self._generate_ast_structure(base, depth + 1) for base in node.bases]
                result["decorator_list"] = [self._generate_ast_structure(decorator, depth + 1)
                                            for decorator in node.decorator_list]
            elif isinstance(node, ast.arguments):
                # 处理参数节点
                result["args"] = [self._generate_ast_structure(arg, depth + 1) for arg in node.args]
                result["defaults"] = [self._generate_ast_structure(default, depth + 1) for default in node.defaults]
                if node.vararg:
                    result["vararg"] = self._generate_ast_structure(node.vararg, depth + 1)
                if node.kwarg:
                    result["kwarg"] = self._generate_ast_structure(node.kwarg, depth + 1)
            elif isinstance(node, ast.arg):
                result["arg"] = node.arg
                if node.annotation:
                    result["annotation"] = self._generate_ast_structure(node.annotation, depth + 1)
            elif isinstance(node, ast.Constant):
                # 统一处理常量节点 (Python 3.8+)
                result["value"] = node.value
                result["kind"] = getattr(node, 'kind', None)
            elif hasattr(ast, 'Str') and isinstance(node, ast.Str):  # Python 3.7及以下兼容
                # 仅在ast.Str存在时使用，避免警告
                result["value"] = node.s
                result["_note"] = "legacy_Str_node"
            elif hasattr(ast, 'Num') and isinstance(node, ast.Num):  # Python 3.7及以下兼容
                # 仅在ast.Num存在时使用，避免警告
                result["value"] = node.n
                result["_note"] = "legacy_Num_node"
            elif isinstance(node, ast.Attribute):
                result["attr"] = node.attr
                result["value"] = self._generate_ast_structure(node.value, depth + 1)
                result["ctx"] = type(node.ctx).__name__
            elif isinstance(node, ast.Subscript):
                result["value"] = self._generate_ast_structure(node.value, depth + 1)
                result["slice"] = self._generate_ast_structure(node.slice, depth + 1)
                result["ctx"] = type(node.ctx).__name__
            elif hasattr(ast, 'Index') and isinstance(node, ast.Index):  # Python 3.8及以下兼容
                result["value"] = self._generate_ast_structure(node.value, depth + 1)
                result["_note"] = "legacy_Index_node"
            elif hasattr(ast, 'Match') and isinstance(node, ast.Match):  # Python 3.10+ 的match语句
                result["subject"] = self._generate_ast_structure(node.subject, depth + 1)
                result["cases"] = [self._generate_ast_structure(case, depth + 1) for case in node.cases]

            # 使用ast.unparse来获取代码表示 (Python 3.9+)
            if hasattr(ast, 'unparse') and hasattr(node, '_fields'):
                try:
                    result["code_snippet"] = ast.unparse(node)
                except Exception:
                    # 如果unparse失败，忽略错误
                    pass

            # 对于其他节点类型，只提取字段名
            if hasattr(node, '_fields'):
                for field in node._fields:
                    if field not in result:  # 避免覆盖已处理的字段
                        field_value = getattr(node, field, None)
                        if field_value is not None:
                            if isinstance(field_value, list):
                                result[field] = [self._generate_ast_structure(item, depth + 1)
                                                 for item in field_value]
                            elif isinstance(field_value, ast.AST):
                                result[field] = self._generate_ast_structure(field_value, depth + 1)
                            else:
                                # 对于基本类型，直接存储
                                try:
                                    json.dumps(field_value)  # 测试是否可序列化
                                    result[field] = field_value
                                except (TypeError, ValueError):
                                    result[field] = str(field_value)

        except Exception as e:
            result["error"] = f"处理节点时出错: {str(e)}"

        return result

    def _get_base_name(self, base: ast.AST) -> str:
        """获取基类名称"""
        if isinstance(base, ast.Name):
            return base.id
        elif isinstance(base, ast.Attribute):
            return ast.unparse(base)
        else:
            return str(type(base).__name__)

    def _get_decorator_name(self, decorator: ast.AST) -> str:
        """获取装饰器名称"""
        if isinstance(decorator, ast.Name):
            return decorator.id
        elif isinstance(decorator, ast.Attribute):
            return ast.unparse(decorator)
        elif isinstance(decorator, ast.Call):
            return self._get_decorator_name(decorator.func)
        else:
            return str(type(decorator).__name__)


def extract_methods_from_python_file(file_path):
    """从Python文件中提取类和方法 - 与method.py保持一致"""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    try:
        tree = ast.parse(content)
    except SyntaxError as e:
        print(f"语法错误在文件 {file_path}: {e}")
        return {}, []

    classes = {}
    global_methods = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            class_name = node.name
            classes[class_name] = []

            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    method_name = item.name
                    # 跳过魔术方法
                    if not method_name.startswith('__') or method_name == '__init__':
                        # 提取方法源代码
                        method_code = ast.get_source_segment(content, item)
                        classes[class_name].append({
                            'name': method_name,
                            'code': method_code
                        })

        elif isinstance(node, ast.FunctionDef):
            method_name = node.name
            # 跳过魔术方法
            if not method_name.startswith('__'):
                # 提取方法源代码
                method_code = ast.get_source_segment(content, node)
                global_methods.append({
                    'name': method_name,
                    'code': method_code
                })

    return classes, global_methods

def safe_json_serialize(obj):
    """安全的JSON序列化函数"""
    if isinstance(obj, (str, int, float, bool, type(None))):
        return obj
    elif isinstance(obj, (list, tuple)):
        return [safe_json_serialize(item) for item in obj]
    elif isinstance(obj, dict):
        return {str(key): safe_json_serialize(value) for key, value in obj.items()}
    else:
        return str(obj)

def process_python_files_for_ast():
    """处理Code文件夹中的所有Python文件生成AST分析"""
    # 获取当前脚本所在目录
    current_dir = Path(__file__).parent
    print(f"当前目录: {current_dir}")

    # 路径配置 - 使用相对路径（与method.py保持一致）
    code_dir = current_dir / "Code"
    result_dir = current_dir / "AST_Result"

    # 检查目录是否存在
    print(f"Code目录: {code_dir} - 存在: {code_dir.exists()}")

    if not code_dir.exists():
        print(f"错误: Code目录不存在: {code_dir}")
        return

    # 创建结果目录
    result_dir.mkdir(exist_ok=True)

    # 初始化AST处理器
    ast_processor = ASTProcessor()

    # 处理每个Python文件
    python_files = list(code_dir.glob("*.py"))
    print(f"找到 {len(python_files)} 个Python文件")

    all_ast_results = {}
    project_summary = {
        "total_files": len(python_files),
        "files_analyzed": 0,
        "files_failed": 0,
        "total_classes": 0,
        "total_methods": 0,
        "total_functions": 0
    }

    for python_file in python_files:
        print(f"处理文件: {python_file.name}")

        try:
            # 提取AST信息
            file_ast = ast_processor.extract_ast_from_python_file(python_file)

            # 为每个Python文件创建目录 - 确保路径正确
            file_result_dir = result_dir / python_file.stem
            file_result_dir.mkdir(exist_ok=True)

            # 保存详细的AST分析结果
            ast_json_file = file_result_dir / "ast_analysis.json"
            with open(ast_json_file, 'w', encoding='utf-8') as f:
                json.dump(file_ast, f, ensure_ascii=False, indent=2)

            print(f"  已保存AST分析: {ast_json_file}")

            # 保存类和方法结构
            classes, global_methods = extract_methods_from_python_file(python_file)

            # 更新项目统计
            project_summary["total_classes"] += len(classes)
            project_summary["total_functions"] += len(global_methods)

            for class_name, methods in classes.items():
                project_summary["total_methods"] += len(methods)

                # 创建类目录 - 确保路径与method_analyzer.py期望的一致
                class_dir = file_result_dir / "classes" / class_name
                class_dir.mkdir(parents=True, exist_ok=True)

                # 保存类信息
                class_json_file = class_dir / "class_info.json"
                with open(class_json_file, 'w', encoding='utf-8') as f:
                    json.dump({
                        "class_name": class_name,
                        "methods_count": len(methods),
                        "methods": [method['name'] for method in methods]
                    }, f, ensure_ascii=False, indent=2)

                # 保存每个方法的详细AST分析 - 关键修改：确保文件名格式正确
                for method in methods:
                    try:
                        # 解析方法代码获取AST节点
                        method_tree = ast.parse(method['code'])
                        if len(method_tree.body) == 1 and isinstance(method_tree.body[0], ast.FunctionDef):
                            func_node = method_tree.body[0]

                            # 使用方法分析函数
                            method_analysis = analyze_specific_method_ast(method['code'], method['name'])

                            # 保存方法AST文件 - 使用正确的命名格式
                            method_ast_file = class_dir / f"{method['name']}_ast.json"
                            with open(method_ast_file, 'w', encoding='utf-8') as f:
                                json.dump(method_analysis, f, ensure_ascii=False, indent=2)

                            print(f"    已保存方法AST: {method_ast_file}")
                        else:
                            print(f"    警告: 无法解析方法 {method['name']} 的AST")
                    except Exception as e:
                        print(f"    处理方法 {method['name']} 时出错: {e}")

            # 保存全局函数 - 同样确保路径正确
            if global_methods:
                global_func_dir = file_result_dir / "global_functions"
                global_func_dir.mkdir(parents=True, exist_ok=True)

                for method in global_methods:
                    try:
                        method_analysis = analyze_specific_method_ast(method['code'], method['name'])

                        # 保存全局函数AST文件 - 使用正确的命名格式
                        func_ast_file = global_func_dir / f"{method['name']}_ast.json"
                        with open(func_ast_file, 'w', encoding='utf-8') as f:
                            json.dump(method_analysis, f, ensure_ascii=False, indent=2)

                        print(f"    已保存全局函数AST: {func_ast_file}")
                    except Exception as e:
                        print(f"    处理全局函数 {method['name']} 时出错: {e}")

            # 添加到总结果
            all_ast_results[python_file.name] = {
                "file_info": {
                    "name": file_ast["file_name"],
                    "path": file_ast["file_path"],
                    "content_length": file_ast["content_length"]
                },
                "summary": {
                    "imports_count": len(file_ast["imports"]),
                    "classes_count": len(file_ast["classes"]),
                    "global_functions_count": len(file_ast["global_functions"]),
                    "global_variables_count": len(file_ast["global_variables"])
                }
            }

            project_summary["files_analyzed"] += 1

        except Exception as e:
            print(f"  处理文件 {python_file.name} 时出错: {e}")
            import traceback
            traceback.print_exc()
            all_ast_results[python_file.name] = {"error": str(e)}
            project_summary["files_failed"] += 1

    # 保存总览文件
    overview_file = result_dir / "ast_analysis_overview.json"
    with open(overview_file, 'w', encoding='utf-8') as f:
        json.dump({
            "project_summary": project_summary,
            "detailed_results": all_ast_results
        }, f, ensure_ascii=False, indent=2)

    print(f"\nAST分析完成！")
    print(f"总览文件: {overview_file}")

    # 打印统计信息
    print(f"\n📊 处理统计:")
    print(f"  - 总文件数: {project_summary['total_files']}")
    print(f"  - 成功分析: {project_summary['files_analyzed']}")
    print(f"  - 失败文件: {project_summary['files_failed']}")
    print(f"  - 总类数: {project_summary['total_classes']}")
    print(f"  - 总方法数: {project_summary['total_methods']}")
    print(f"  - 总函数数: {project_summary['total_functions']}")


def analyze_specific_method_ast(method_code: str, method_name: str = "unknown_method") -> Dict[str, Any]:
    """分析特定方法的AST结构 - 修复版本"""
    ast_processor = ASTProcessor()

    try:
        # 解析方法代码
        method_tree = ast.parse(method_code)

        if len(method_tree.body) == 1 and isinstance(method_tree.body[0], ast.FunctionDef):
            func_node = method_tree.body[0]
            func_info = ast_processor._extract_function_info(func_node, method_code)

            return {
                "method_name": method_name,
                "code": method_code,
                "ast_analysis": func_info,
                "raw_ast": ast_processor._generate_ast_structure(func_node)
            }
        else:
            return {
                "method_name": method_name,
                "error": "不是有效的函数定义",
                "code": method_code,
                "ast_structure": ast_processor._generate_ast_structure(method_tree)
            }

    except Exception as e:
        return {
            "method_name": method_name,
            "error": str(e),
            "code": method_code
        }


if __name__ == "__main__":
    process_python_files_for_ast()