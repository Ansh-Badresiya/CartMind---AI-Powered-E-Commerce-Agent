from langchain_groq import ChatGroq


class LlmClient:
    """Groq chat client — wraps ChatGroq creation.

    Created once in di.py and injected into LLM components.
    """

    def __init__(self, api_key: str, model: str = "openai/gpt-oss-20b") -> None:
        self.chat_groq = ChatGroq(
            model=model,
            groq_api_key=api_key,
            temperature=0.3,
        )
