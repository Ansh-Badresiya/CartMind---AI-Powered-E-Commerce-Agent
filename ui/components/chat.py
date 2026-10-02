"""
ui/components/chat.py
---------------------
Chat rendering components:
- Welcome / empty-state screen with prompt suggestions
- Message history renderer
- Individual user / assistant bubble renderers
- Typing indicator
"""

from __future__ import annotations

import streamlit as st

from ui.config import SUGGESTED_PROMPTS, WELCOME_MESSAGE
from ui.session import Message, get_messages, set_pending_prompt


# ---------------------------------------------------------------------------
# Public entry point
# ---------------------------------------------------------------------------

def render_chat_area(is_waiting: bool) -> None:
    """
    Render the full chat area.
    Shows the welcome screen when there are no messages, otherwise
    renders the message history and (optionally) a typing indicator.
    """
    messages = get_messages()

    if not messages:
        _render_welcome()
        return

    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for msg in messages:
        _render_message(msg)

    if is_waiting:
        _render_typing_indicator()

    st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Welcome / empty state
# ---------------------------------------------------------------------------

def _render_welcome() -> None:
    st.markdown(
        """
        <div class="welcome-container">
            <div class="welcome-icon">🛒</div>
            <div class="welcome-title">ShopBot AI</div>
            <div class="welcome-subtitle">
                Your intelligent e-commerce assistant — ask me anything!
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Suggested prompts in a 3-column grid
    cols = st.columns(3, gap="small")
    for i, prompt in enumerate(SUGGESTED_PROMPTS):
        with cols[i % 3]:
            if st.button(
                f"{prompt['icon']}  {prompt['label']}",
                key=f"suggestion_{i}",
                use_container_width=True,
            ):
                set_pending_prompt(prompt["label"])
                st.rerun()


# ---------------------------------------------------------------------------
# Message rendering
# ---------------------------------------------------------------------------

def _render_message(msg: Message) -> None:
    if msg.role == "user":
        _render_user_bubble(msg.content)
    else:
        _render_assistant_bubble(msg.content, msg.sources, msg.is_error)


def _render_user_bubble(content: str) -> None:
    # Escape HTML in user content for safety
    safe_content = (
        content
        .replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    st.markdown(
        f"""
        <div class="msg-user">
            <div class="msg-user-bubble">{safe_content}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_assistant_bubble(
    content: str,
    sources: list[str],
    is_error: bool = False,
) -> None:
    error_class = "error" if is_error else ""

    # Build sources HTML
    sources_html = ""
    if sources:
        badges = "".join(
            f'<span class="source-badge">📦 {src}</span>' for src in sources
        )
        sources_html = f'<div class="sources-row">{badges}</div>'

    # Render content via st.markdown for proper markdown support,
    # but wrap it in a styled container using a placeholder approach.
    # We use a container + custom HTML shell + st.markdown for the body.
    with st.container():
        st.markdown(
            f"""
            <div class="msg-assistant">
                <div class="msg-avatar">🤖</div>
                <div class="msg-assistant-bubble {error_class}">
            """,
            unsafe_allow_html=True,
        )
        # Use st.markdown for the actual content so markdown renders properly
        st.markdown(content)
        if sources_html:
            st.markdown(sources_html, unsafe_allow_html=True)
        st.markdown("</div></div>", unsafe_allow_html=True)


def _render_typing_indicator() -> None:
    st.markdown(
        """
        <div class="typing-indicator">
            <div class="msg-avatar" style="width:36px;height:36px;border-radius:50%;
                 background:linear-gradient(135deg,#06b6d4,#0891b2);
                 display:flex;align-items:center;justify-content:center;font-size:1rem;">
                🤖
            </div>
            <div class="typing-bubble">
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
                <div class="typing-dot"></div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
