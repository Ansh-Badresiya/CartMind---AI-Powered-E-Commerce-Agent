"""
ui/api_client.py
----------------
Thin HTTP client that wraps all calls to the FastAPI backend.
Returns typed dataclasses so the rest of the UI never deals with raw dicts.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field

import requests

from ui.config import API_CHAT_ENDPOINT, API_TIMEOUT_SECONDS


# ---------------------------------------------------------------------------
# Response models (plain dataclasses — no FastAPI/Pydantic dependency in UI)
# ---------------------------------------------------------------------------

@dataclass
class ChatResponse:
    answer: str
    session_id: str
    sources: list[str] = field(default_factory=list)


@dataclass
class APIError:
    message: str
    status_code: int | None = None


# ---------------------------------------------------------------------------
# Client
# ---------------------------------------------------------------------------

class AgentAPIClient:
    """
    Stateless client for the e-commerce agent REST API.

    Usage::

        client = AgentAPIClient()
        result = client.chat("Tell me about laptops", session_id="abc-123")
        if isinstance(result, APIError):
            # handle error
            ...
        else:
            print(result.answer)
    """

    def __init__(self, base_timeout: int = API_TIMEOUT_SECONDS) -> None:
        self._timeout = base_timeout
        self._session = requests.Session()
        self._session.headers.update({"Content-Type": "application/json"})

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def chat(
        self,
        message: str,
        session_id: str | None = None,
    ) -> ChatResponse | APIError:
        """
        Send a message to the agent and return a typed response.

        Args:
            message:    The user's chat message.
            session_id: Conversation thread ID. Auto-generated if None.

        Returns:
            ChatResponse on success, APIError on failure.
        """
        payload = {
            "message": message,
            "session_id": session_id or str(uuid.uuid4()),
        }
        try:
            resp = self._session.post(
                API_CHAT_ENDPOINT,
                json=payload,
                timeout=self._timeout,
            )
            resp.raise_for_status()
            data = resp.json()
            return ChatResponse(
                answer=data["answer"],
                session_id=data["session_id"],
                sources=data.get("sources", []),
            )
        except requests.exceptions.ConnectionError:
            return APIError(
                message=(
                    "⚠️ Cannot reach the agent API. "
                    "Make sure the Docker services are running (`docker compose up -d`)."
                )
            )
        except requests.exceptions.Timeout:
            return APIError(
                message="⏱️ The request timed out. The agent is taking too long — please try again."
            )
        except requests.exceptions.HTTPError as exc:
            try:
                detail = exc.response.json().get("detail", str(exc))
            except Exception:
                detail = str(exc)
            return APIError(
                message=f"❌ API error: {detail}",
                status_code=exc.response.status_code,
            )
        except Exception as exc:  # noqa: BLE001
            return APIError(message=f"❌ Unexpected error: {exc}")

    def health_check(self) -> bool:
        """Return True if the API is reachable."""
        try:
            resp = self._session.get(
                API_CHAT_ENDPOINT.replace("/chat", "/docs"),
                timeout=5,
            )
            return resp.status_code < 500
        except Exception:  # noqa: BLE001
            return False
