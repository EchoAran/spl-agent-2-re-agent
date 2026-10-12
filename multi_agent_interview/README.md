# Multi Agent Interview

面向 GitHub 仓库访谈的多代理系统，目标是通过“访谈代理 + 仓库受访代理”对话，稳定提取仓库细节。

## 架构边界

- 主框架（会话编排）：
  - `backend/app/session_manager.py`
  - `backend/app/orchestrator.py`
- 访谈技能执行（可替换）：
  - `backend/app/agents.py` 中的 `InterviewerSkillAgent`
  - `backend/skills/*`
- 仓库问答适配层（与主框架解耦）：
  - `backend/app/repository_qa.py`
  - 默认实现 `SPLRepositoryQAAdapter` 调用 `spl_agent`

主框架只依赖 `AgentRuntime` 协议，不直接绑定某个技能实现或某个代码理解后端。

## 会话接口

- 创建会话：`POST /api/sessions`
- 请求参数：
  - `github_repo_url`：目标仓库地址
  - `project_name`：可选项目名
  - `interview_skill_name`：可选，默认 `requirements-elicitation`

## 运行中间产物

- `backend/runtime/session_cache/`：会话消息缓存
- `backend/runtime/llm_io.jsonl`：主访谈模型 I/O 日志
- `backend/runtime/spl_cache/`：`spl_agent` 的构建缓存（在访谈模式下）

上述目录均为可重建产物，已在仓库 `.gitignore` 忽略。
