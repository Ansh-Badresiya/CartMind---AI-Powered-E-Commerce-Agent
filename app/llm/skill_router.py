"""LLM-based skill router - replaces keyword matching in route_skill node."""

from langchain_core.language_models import BaseChatModel
from langchain_core.messages import HumanMessage, SystemMessage

from app.llm.prompts import SKILL_ROUTER_PROMPT
from app.llm.types import SkillResult


class SkillRouter:
    """Classifies user messages into 'qa', 'order', or 'track' skill using an LLM.

    Uses the chat provider's structured output (with_structured_output) for
    guaranteed JSON schema compliance.
    """

    def __init__(self, llm: BaseChatModel) -> None:
        self._llm = llm.with_structured_output(SkillResult)

    async def classify(self, message: str) -> SkillResult:
        messages = [
            SystemMessage(content=SKILL_ROUTER_PROMPT),
            HumanMessage(content=message),
        ]
        return await self._llm.ainvoke(messages)
