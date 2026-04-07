from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import Any, Dict, List, Optional

from .models import FunctionSemantics


INPUT_OUTPUT_RE = re.compile(
    r'<REF>\s*(?P<name>.*?)\s*</REF>:\s*(?P<type>.*?)\s*"(?P<desc>.*)"'
)
DEFINE_RE = re.compile(r'^\[DEFINE_WORKER:\s*"(?P<summary>.*)"\s+(?P<name>[^\]]+)\]$')
ALT_RE = re.compile(r'^\[ALTERNATIVE_FLOW:\s*(?P<condition>.*)\]$')
EXC_RE = re.compile(r'^\[EXCEPTION_FLOW:\s*(?P<condition>.*)\]$')
COMMAND_RE = re.compile(r'^\[COMMAND\s+(?P<command>.*?)\s+RESULT\s+(?P<result>.*?)\]$')
LOG_RE = re.compile(r'^\[LOG\s+"(?P<log>.*)"\]$')
THROW_RE = re.compile(r'^\[THROW\s+(?P<name>\S+)\s+"(?P<desc>.*)"\]$')


@dataclass
class LegacyFunctionDocument:
    semantics: FunctionSemantics
    raw_text: str


class LegacySPLParser:
    def parse_file(self, file_path: str | Path) -> LegacyFunctionDocument:
        path = Path(file_path)
        text = path.read_text(encoding="utf-8")
        return self.parse_text(text)

    def parse_text(self, text: str) -> LegacyFunctionDocument:
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        define_match = next((DEFINE_RE.match(line) for line in lines if DEFINE_RE.match(line)), None)
        if not define_match:
            raise ValueError("Invalid SPL: missing DEFINE_WORKER header")

        summary = define_match.group("summary").strip()
        worker_name = define_match.group("name").strip()

        inputs = self._parse_named_block(lines, "INPUTS")
        outputs = self._parse_named_block(lines, "OUTPUTS")
        main_flow = self._parse_main_flow(lines)
        alternative_flows = self._parse_alternative_flows(lines)
        exception_flows = self._parse_exception_flows(lines)

        semantics = FunctionSemantics(
            worker_name=worker_name,
            brief_description=summary,
            inputs=inputs,
            outputs=outputs,
            main_flow=main_flow,
            alternative_flows=alternative_flows,
            exception_flows=exception_flows,
            raw_json={
                "worker_name": worker_name,
                "brief_description": summary,
                "inputs": inputs,
                "outputs": outputs,
                "main_flow": main_flow,
                "alternative_flows": alternative_flows,
                "exception_flows": exception_flows,
            },
        )
        return LegacyFunctionDocument(semantics=semantics, raw_text=text)

    def _parse_named_block(self, lines: List[str], name: str) -> List[Dict[str, str]]:
        start = self._find_line(lines, f"[{name}]")
        end = self._find_line(lines, f"[END_{name}]")
        if start == -1 or end == -1 or end <= start:
            return []

        items: List[Dict[str, str]] = []
        for line in lines[start + 1:end]:
            match = INPUT_OUTPUT_RE.match(line)
            if match:
                items.append(
                    {
                        "name": match.group("name").strip(),
                        "type": match.group("type").strip(),
                        "desc": match.group("desc").strip(),
                    }
                )
        return items

    def _parse_main_flow(self, lines: List[str]) -> List[Dict[str, str]]:
        start = self._find_line(lines, "[MAIN_FLOW]")
        end = self._find_line(lines, "[END_MAIN_FLOW]")
        if start == -1 or end == -1 or end <= start:
            return []
        steps: List[Dict[str, str]] = []
        for line in lines[start + 1:end]:
            match = COMMAND_RE.match(line)
            if match:
                steps.append(
                    {
                        "command": match.group("command").strip(),
                        "result": match.group("result").strip(),
                    }
                )
        return steps

    def _parse_alternative_flows(self, lines: List[str]) -> List[Dict[str, Any]]:
        flows: List[Dict[str, Any]] = []
        idx = 0
        while idx < len(lines):
            alt_match = ALT_RE.match(lines[idx])
            if not alt_match:
                idx += 1
                continue
            condition = alt_match.group("condition").strip()
            steps: List[Dict[str, str]] = []
            idx += 1
            while idx < len(lines) and lines[idx] != "[END_ALTERNATIVE_FLOW]":
                cmd_match = COMMAND_RE.match(lines[idx])
                if cmd_match:
                    steps.append(
                        {
                            "command": cmd_match.group("command").strip(),
                            "result": cmd_match.group("result").strip(),
                        }
                    )
                idx += 1
            flows.append({"condition": condition, "steps": steps})
            idx += 1
        return flows

    def _parse_exception_flows(self, lines: List[str]) -> List[Dict[str, Any]]:
        flows: List[Dict[str, Any]] = []
        idx = 0
        while idx < len(lines):
            exc_match = EXC_RE.match(lines[idx])
            if not exc_match:
                idx += 1
                continue
            condition = exc_match.group("condition").strip()
            log = ""
            throw_name = "Exception"
            throw_desc = ""
            idx += 1
            while idx < len(lines) and lines[idx] != "[END_EXCEPTION_FLOW]":
                log_match = LOG_RE.match(lines[idx])
                if log_match:
                    log = log_match.group("log").strip()
                throw_match = THROW_RE.match(lines[idx])
                if throw_match:
                    throw_name = throw_match.group("name").strip()
                    throw_desc = throw_match.group("desc").strip()
                idx += 1
            flows.append(
                {
                    "condition": condition,
                    "log": log,
                    "throw": {"name": throw_name, "desc": throw_desc},
                }
            )
            idx += 1
        return flows

    def _find_line(self, lines: List[str], target: str) -> int:
        for idx, line in enumerate(lines):
            if line == target:
                return idx
        return -1


def infer_calls_from_semantics(semantics: FunctionSemantics) -> List[str]:
    seen: List[str] = []
    texts = [step.get("command", "") for step in semantics.main_flow]
    for flow in semantics.alternative_flows:
        texts.extend(step.get("command", "") for step in flow.get("steps", []))
    for text in texts:
        for match in re.findall(r"<SPL>(.*?)</SPL>", text):
            if match not in seen:
                seen.append(match)
        for match in re.findall(r"\b([A-Za-z_][A-Za-z0-9_]*)\s*\(", text):
            if match not in {"if", "for", "while", "int", "str", "dict", "list", "max", "min"} and match not in seen:
                seen.append(match)
    return seen

