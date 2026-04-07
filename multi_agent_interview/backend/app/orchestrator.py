from __future__ import annotations

from dataclasses import dataclass, field
from typing import AsyncGenerator

from .agents import AgentRuntime
from .models import ChatMessage, InterviewRoundContext


@dataclass
class InterviewOrchestrator:
    interviewer: AgentRuntime
    respondents: list[AgentRuntime]
    max_rounds: int = 24
    transcript: list[ChatMessage] = field(default_factory=list)
    round_index: int = 0

    async def run_round_stream(
        self,
        user_input: str,
        enabled_agent_ids: list[str],
        session_status: str,
        session_id: str,
    ) -> AsyncGenerator[tuple[ChatMessage, bool, str | None], None]:
        self.round_index += 1
        context = InterviewRoundContext(
            round_index=self.round_index,
            user_input=user_input,
            transcript=self.transcript,
            enabled_agent_ids=enabled_agent_ids,
            metadata={"session_status": session_status, "session_id": session_id},
        )

        interviewer_question = await self.interviewer.respond(
            context=context,
            prompt="请继续访谈。",
        )
        self.transcript.append(interviewer_question)
        text = interviewer_question.text
        if "[[INTERVIEW_COMPLETE]]" in text:
            yield interviewer_question, True, "系统代理判定访谈完成"
            return
        yield interviewer_question, False, None

        for respondent in self.respondents:
            if respondent.id not in enabled_agent_ids:
                continue
            respondent_context = InterviewRoundContext(
                round_index=self.round_index,
                user_input=user_input,
                transcript=self.transcript,
                enabled_agent_ids=enabled_agent_ids,
                metadata={"session_status": session_status, "session_id": session_id},
            )
            answer = await respondent.respond(
                context=respondent_context,
                prompt=interviewer_question.text,
            )
            self.transcript.append(answer)
            yield answer, False, None

        if self.round_index >= self.max_rounds:
            finish_message = ChatMessage(
                id=f"system-max-round-{self.round_index}",
                agent_id=self.interviewer.id,
                agent_name=self.interviewer.name,
                role=self.interviewer.role,
                text=f"达到安全轮次上限 {self.max_rounds}，自动结束",
                round_index=self.round_index,
            )
            self.transcript.append(finish_message)
            yield finish_message, True, finish_message.text
