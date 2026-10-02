"""
ui/components/header.py
-----------------------
Top-of-page header bar showing page title and current skill context.
"""

from __future__ import annotations

import streamlit as st

from ui.session import get_messages


def render_header() -> None:
    """Render the page header with dynamic message count badge."""
    messages = get_messages()
    msg_count = len(messages)

    count_badge = ""
    if msg_count > 0:
        turns = msg_count // 2
        count_badge = (
            f'<span style="'
            f"background:rgba(124,58,237,0.15);"
            f"border:1px solid rgba(124,58,237,0.3);"
            f"border-radius:20px;"
            f"padding:0.2rem 0.6rem;"
            f"font-size:0.75rem;"
            f"color:#a78bfa;"
            f"font-weight:500;"
            f'">{turns} turn{"s" if turns != 1 else ""}</span>'
        )

    st.markdown(
        f"""
        <div style="
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0.75rem 0 1rem;
            border-bottom: 1px solid rgba(124,58,237,0.15);
            margin-bottom: 1rem;
        ">
            <div style="display:flex; align-items:center; gap:0.6rem;">
                <span style="font-size:1.5rem;">🤖</span>
                <div>
                    <div style="
                        font-size:1.1rem;
                        font-weight:700;
                        background:linear-gradient(90deg,#7c3aed,#06b6d4);
                        -webkit-background-clip:text;
                        -webkit-text-fill-color:transparent;
                        background-clip:text;
                    ">ShopBot AI</div>
                    <div style="font-size:0.72rem; color:#475569;">
                        E-commerce assistant · LangGraph Agent
                    </div>
                </div>
            </div>
            <div style="display:flex; align-items:center; gap:0.5rem;">
                {count_badge}
                <span style="
                    padding:0.25rem 0.75rem;
                    background:rgba(6,182,212,0.1);
                    border:1px solid rgba(6,182,212,0.25);
                    border-radius:20px;
                    font-size:0.72rem;
                    color:#22d3ee;
                    font-weight:500;
                ">● Live</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
