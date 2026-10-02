"""
ui/components/sidebar.py
------------------------
Sidebar component: logo, new-chat button, category quick-filters,
API status indicator, and session info.
"""

from __future__ import annotations

import streamlit as st

from ui.api_client import AgentAPIClient
from ui.config import PRODUCT_CATEGORIES
from ui.session import get_session_id, new_conversation, set_pending_prompt


def render_sidebar(api_client: AgentAPIClient) -> None:
    """Render the full left sidebar."""
    with st.sidebar:
        _render_logo()
        _render_new_chat_button()
        _render_category_section()
        _render_spacer()
        _render_status_section(api_client)
        _render_session_info()


# ---------------------------------------------------------------------------
# Private helpers
# ---------------------------------------------------------------------------

def _render_logo() -> None:
    st.markdown(
        """
        <div class="shopbot-header">
            <div class="shopbot-logo">🛒</div>
            <div>
                <div class="shopbot-title">ShopBot AI</div>
                <div class="shopbot-subtitle">Powered by LangGraph + Groq</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_new_chat_button() -> None:
    # type="primary" maps to [data-testid="baseButton-primary"] in CSS → purple gradient
    if st.button("✦  New Conversation", key="new_chat_btn", type="primary", use_container_width=True):
        new_conversation()
        st.rerun()


def _render_category_section() -> None:
    st.markdown(
        '<div class="sidebar-section-label">Browse Categories</div>',
        unsafe_allow_html=True,
    )

    # 2-column grid of clickable category buttons.
    #
    # WHY buttons and not a selectbox?
    # Streamlit prohibits modifying a widget's session_state key after it has
    # been rendered in the same script run — any reset silently fails, so the
    # selectbox never returns to the placeholder and fires every rerun in a
    # loop. Buttons have no such limitation: each click is a clean, one-shot
    # event with no state to reset.
    left_col, right_col = st.columns(2, gap="small")
    for i, cat in enumerate(PRODUCT_CATEGORIES):
        col = left_col if i % 2 == 0 else right_col
        with col:
            if st.button(
                f"{cat['icon']} {cat['label']}",
                key=f"cat_btn_{cat['label']}",
                use_container_width=True,
                type="secondary",   # ghost chip style via CSS
            ):
                set_pending_prompt(f"Tell me about {cat['label'].lower()}")
                st.rerun()


def _render_spacer() -> None:
    st.markdown("<hr class='custom-divider'>", unsafe_allow_html=True)


def _render_status_section(api_client: AgentAPIClient) -> None:
    st.markdown(
        '<div class="sidebar-section-label">System Status</div>',
        unsafe_allow_html=True,
    )
    is_online = api_client.health_check()
    if is_online:
        st.markdown(
            """
            <div class="status-bar">
                <span class="status-online">
                    <span class="status-dot online"></span>
                    API Online
                </span>
                <div style="color:#475569; font-size:0.72rem; margin-top:0.3rem;">
                    FastAPI · LangGraph · ChromaDB
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <div class="status-bar">
                <span class="status-offline">
                    <span class="status-dot offline"></span>
                    API Offline
                </span>
                <div style="color:#475569; font-size:0.72rem; margin-top:0.3rem;">
                    Run: <code>docker compose up -d</code>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def _render_session_info() -> None:
    session_id = get_session_id()
    st.markdown(
        f"""
        <div style="margin-top:0.75rem;">
            <div class="sidebar-section-label">Session ID</div>
            <div class="session-pill">{session_id[:8]}…{session_id[-4:]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
