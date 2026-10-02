"""
ui/session.py
-------------
All Streamlit session-state management in one place.
Centralising st.session_state keys avoids typo bugs and makes
state mutation easy to audit.
"""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import Literal

import streamlit as st


# ---------------------------------------------------------------------------
# Message model
# ---------------------------------------------------------------------------

Role = Literal["user", "assistant"]


@dataclass
class Message:
    role: Role
    content: str
    sources: list[str] = field(default_factory=list)
    is_error: bool = False


# ---------------------------------------------------------------------------
# Session state keys
# ---------------------------------------------------------------------------

_SESSION_ID_KEY = "session_id"
_MESSAGES_KEY = "messages"
_WAITING_KEY = "waiting_for_response"
_PENDING_PROMPT_KEY = "pending_prompt"


# ---------------------------------------------------------------------------
# Initialisation
# ---------------------------------------------------------------------------

def init_session() -> None:
    """
    Initialise all session-state keys on first run.
    Safe to call on every re-run — only sets keys that don't exist yet.
    """
    if _SESSION_ID_KEY not in st.session_state:
        st.session_state[_SESSION_ID_KEY] = str(uuid.uuid4())
    if _MESSAGES_KEY not in st.session_state:
        st.session_state[_MESSAGES_KEY] = []
    if _WAITING_KEY not in st.session_state:
        st.session_state[_WAITING_KEY] = False
    if _PENDING_PROMPT_KEY not in st.session_state:
        st.session_state[_PENDING_PROMPT_KEY] = None


# ---------------------------------------------------------------------------
# Accessors / mutators
# ---------------------------------------------------------------------------

def get_session_id() -> str:
    return st.session_state[_SESSION_ID_KEY]


def get_messages() -> list[Message]:
    return st.session_state[_MESSAGES_KEY]


def add_message(role: Role, content: str, sources: list[str] | None = None, is_error: bool = False) -> None:
    st.session_state[_MESSAGES_KEY].append(
        Message(role=role, content=content, sources=sources or [], is_error=is_error)
    )


def is_waiting() -> bool:
    return st.session_state[_WAITING_KEY]


def set_waiting(value: bool) -> None:
    st.session_state[_WAITING_KEY] = value


def get_pending_prompt() -> str | None:
    return st.session_state[_PENDING_PROMPT_KEY]


def set_pending_prompt(prompt: str | None) -> None:
    st.session_state[_PENDING_PROMPT_KEY] = prompt


def new_conversation() -> None:
    """Reset to a fresh conversation (new session ID, cleared history)."""
    st.session_state[_SESSION_ID_KEY] = str(uuid.uuid4())
    st.session_state[_MESSAGES_KEY] = []
    st.session_state[_WAITING_KEY] = False
    st.session_state[_PENDING_PROMPT_KEY] = None
