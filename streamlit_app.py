"""
streamlit_app.py
----------------
Entry point for the Streamlit UI.

Run with:
    streamlit run streamlit_app.py

The UI talks to the FastAPI backend at http://localhost:8000 by default.
Override with the AGENT_API_URL environment variable.
"""

from __future__ import annotations

import streamlit as st
import streamlit.components.v1 as components

from ui.api_client import AgentAPIClient, APIError
from ui.components.chat import render_chat_area
from ui.components.header import render_header
from ui.components.sidebar import render_sidebar
from ui.config import PAGE_ICON, PAGE_LAYOUT, PAGE_TITLE
from ui.session import (
    add_message,
    get_pending_prompt,
    get_session_id,
    init_session,
    is_waiting,
    set_pending_prompt,
    set_waiting,
)
from ui.styles import inject_styles

# ---------------------------------------------------------------------------
# Page config — MUST be the first Streamlit call
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout=PAGE_LAYOUT,
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Bootstrap
# ---------------------------------------------------------------------------
inject_styles()
init_session()

# ---------------------------------------------------------------------------
# Sidebar auto-expand fix (JavaScript-based)
# ---------------------------------------------------------------------------
# Streamlit persists the sidebar open/closed state in the browser's
# localStorage, which overrides initial_sidebar_state="expanded" on refresh.
# The only reliable fix is JavaScript: detect if the sidebar is collapsed and
# programmatically click the expand button.
#
# window.parent.__cartmindSidebarReady persists across Streamlit reruns
# (which don't reload the page) but is reset on actual browser refresh.
# This means we auto-expand exactly once per page load — not on every rerun.
components.html(
    """
    <script>
    (function () {
        function expandSidebar() {
            // stSidebarCollapsedControl only exists in the DOM when sidebar
            // is collapsed, so clicking it is always safe (no double-toggle).
            var btn = window.parent.document.querySelector(
                '[data-testid="stSidebarCollapsedControl"]'
            );
            if (btn) {
                btn.click();
                return true;
            }
            return false;
        }

        if (!window.parent.__cartmindSidebarReady) {
            window.parent.__cartmindSidebarReady = true;
            // Try at 300ms (fast machines) and 900ms (slow / first load).
            setTimeout(function () {
                if (!expandSidebar()) {
                    setTimeout(expandSidebar, 600);
                }
            }, 300);
        }
    })();
    </script>
    """,
    height=0,
    scrolling=False,
)

# Singleton API client (cached for the lifetime of the browser session)
@st.cache_resource
def get_api_client() -> AgentAPIClient:
    return AgentAPIClient()


api_client = get_api_client()

# ---------------------------------------------------------------------------
# Layout
# ---------------------------------------------------------------------------
render_sidebar(api_client)

# Main content column (slightly padded)
with st.container():
    render_header()
    render_chat_area(is_waiting=is_waiting())

# ---------------------------------------------------------------------------
# Handle pending prompt injected by sidebar / suggestion chips
# ---------------------------------------------------------------------------
pending = get_pending_prompt()
if pending:
    set_pending_prompt(None)
    # Add to history and trigger agent call
    add_message("user", pending)
    set_waiting(True)
    st.rerun()

# ---------------------------------------------------------------------------
# Chat input
# ---------------------------------------------------------------------------
user_input: str | None = st.chat_input(
    placeholder="Ask about products, place an order, or track your delivery…",
    disabled=is_waiting(),
    key="chat_input",
)

if user_input and user_input.strip():
    add_message("user", user_input.strip())
    set_waiting(True)
    st.rerun()

# ---------------------------------------------------------------------------
# Agent call (runs only when waiting=True and last message is from user)
# ---------------------------------------------------------------------------
if is_waiting():
    from ui.session import get_messages  # local import avoids circular at top

    messages = get_messages()
    # Find the last user message to send
    last_user_msg = next(
        (m.content for m in reversed(messages) if m.role == "user"), None
    )

    if last_user_msg:
        with st.spinner(""):
            result = api_client.chat(
                message=last_user_msg,
                session_id=get_session_id(),
            )

        if isinstance(result, APIError):
            add_message("assistant", result.message, is_error=True)
        else:
            add_message(
                "assistant",
                result.answer,
                sources=result.sources,
            )

    set_waiting(False)
    st.rerun()
