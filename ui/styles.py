"""
ui/styles.py
------------
All custom CSS injected into the Streamlit page.
Keeping CSS in one module makes theming easy to change globally.
"""

from __future__ import annotations

import streamlit as st


_CSS = """
/* ─── Google Fonts ─────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ─── Root / Page ───────────────────────────────────────────────────────── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif !important;
}

/* ─── Hide Streamlit chrome — keep sidebar toggle visible ──────────────── */
#MainMenu { visibility: hidden; }
footer { visibility: hidden; }
.stDeployButton { display: none; }

/* Hide the top toolbar (deploy/share buttons) but NOT the sidebar toggle */
[data-testid="stToolbar"] { visibility: hidden !important; }

/* Make the header bar transparent so it doesn't block the dark background */
[data-testid="stHeader"] {
    background: transparent !important;
    border-bottom: none !important;
}

/* Make the sidebar expand button (>) visible and styled on dark background */
[data-testid="stSidebarCollapsedControl"] {
    background: rgba(22, 27, 46, 0.95) !important;
    border: 1px solid rgba(124, 58, 237, 0.35) !important;
    border-radius: 0 8px 8px 0 !important;
    backdrop-filter: blur(10px);
    box-shadow: 2px 0 12px rgba(124, 58, 237, 0.2) !important;
}

[data-testid="stSidebarCollapsedControl"]:hover {
    background: rgba(124, 58, 237, 0.2) !important;
    border-color: rgba(124, 58, 237, 0.6) !important;
}

[data-testid="stSidebarCollapsedControl"] svg {
    color: #a78bfa !important;
    fill: #a78bfa !important;
}

/* ─── Page background ───────────────────────────────────────────────────── */
.stApp {
    background: linear-gradient(135deg, #0a0e1a 0%, #0f1629 50%, #0d1117 100%);
    min-height: 100vh;
}

/* ─── Sidebar ───────────────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d1117 0%, #161b2e 100%) !important;
    border-right: 1px solid rgba(124, 58, 237, 0.2);
}

[data-testid="stSidebar"] .block-container {
    padding: 1.5rem 1rem !important;
}

/* ─── App header (logo row) ─────────────────────────────────────────────── */
.shopbot-header {
    display: flex;
    align-items: center;
    gap: 0.75rem;
    padding: 1.25rem 1rem 1rem;
    border-bottom: 1px solid rgba(124, 58, 237, 0.25);
    margin-bottom: 1rem;
}

.shopbot-logo {
    font-size: 2rem;
    line-height: 1;
}

.shopbot-title {
    font-size: 1.4rem;
    font-weight: 700;
    background: linear-gradient(90deg, #7c3aed, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    letter-spacing: -0.02em;
}

.shopbot-subtitle {
    font-size: 0.75rem;
    color: #64748b;
    margin-top: 0.1rem;
}

/* ─── Buttons — primary (New Chat) ─────────────────────────────────────── */
[data-testid="baseButton-primary"] {
    width: 100%;
    background: linear-gradient(135deg, #7c3aed, #6d28d9) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-weight: 600 !important;
    font-size: 0.875rem !important;
    padding: 0.6rem 1rem !important;
    transition: all 0.2s ease !important;
    letter-spacing: 0.01em;
}

[data-testid="baseButton-primary"]:hover {
    background: linear-gradient(135deg, #6d28d9, #5b21b6) !important;
    transform: translateY(-1px);
    box-shadow: 0 4px 20px rgba(124, 58, 237, 0.4) !important;
}

/* ─── Buttons — secondary (category chips in sidebar) ───────────────────── */
[data-testid="stSidebar"] [data-testid="baseButton-secondary"] {
    background: rgba(124, 58, 237, 0.08) !important;
    border: 1px solid rgba(124, 58, 237, 0.22) !important;
    color: #a78bfa !important;
    border-radius: 8px !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    padding: 0.3rem 0.4rem !important;
    transition: all 0.15s ease !important;
    width: 100%;
    text-align: left;
}

[data-testid="stSidebar"] [data-testid="baseButton-secondary"]:hover {
    background: rgba(124, 58, 237, 0.2) !important;
    border-color: rgba(124, 58, 237, 0.45) !important;
    color: #c4b5fd !important;
    transform: translateY(-1px);
    box-shadow: 0 2px 10px rgba(124, 58, 237, 0.15) !important;
}

/* ─── Buttons — secondary in main area (suggestion prompt cards) ─────────── */
[data-testid="stMain"] [data-testid="baseButton-secondary"] {
    background: rgba(30, 33, 48, 0.8) !important;
    border: 1px solid rgba(124, 58, 237, 0.2) !important;
    color: #cbd5e1 !important;
    border-radius: 12px !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    padding: 0.85rem 1rem !important;
    transition: all 0.2s ease !important;
    text-align: left;
    width: 100%;
    backdrop-filter: blur(10px);
    min-height: 64px;
}

[data-testid="stMain"] [data-testid="baseButton-secondary"]:hover {
    background: rgba(124, 58, 237, 0.15) !important;
    border-color: rgba(124, 58, 237, 0.5) !important;
    color: #e2e8f0 !important;
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(124, 58, 237, 0.2) !important;
}

/* ─── Category chips (sidebar) ──────────────────────────────────────────── */
.category-chip {
    display: inline-flex;
    align-items: center;
    gap: 0.4rem;
    padding: 0.4rem 0.8rem;
    border-radius: 20px;
    background: rgba(124, 58, 237, 0.12);
    border: 1px solid rgba(124, 58, 237, 0.25);
    color: #a78bfa;
    font-size: 0.8rem;
    font-weight: 500;
    cursor: pointer;
    transition: all 0.15s ease;
    margin: 0.2rem;
    text-decoration: none;
    white-space: nowrap;
}

.category-chip:hover {
    background: rgba(124, 58, 237, 0.25);
    border-color: rgba(124, 58, 237, 0.5);
    color: #c4b5fd;
    transform: translateY(-1px);
}

/* ─── Chat messages area ────────────────────────────────────────────────── */
.chat-container {
    max-width: 800px;
    margin: 0 auto;
    padding: 1rem 0 2rem;
}

/* ─── User message bubble ───────────────────────────────────────────────── */
.msg-user {
    display: flex;
    justify-content: flex-end;
    margin: 0.75rem 0;
    animation: slideInRight 0.2s ease;
}

.msg-user-bubble {
    max-width: 75%;
    background: linear-gradient(135deg, #7c3aed 0%, #6d28d9 100%);
    color: #fff;
    padding: 0.85rem 1.1rem;
    border-radius: 18px 18px 4px 18px;
    font-size: 0.9rem;
    line-height: 1.6;
    box-shadow: 0 4px 15px rgba(124, 58, 237, 0.3);
    word-wrap: break-word;
}

/* ─── Assistant message bubble ──────────────────────────────────────────── */
.msg-assistant {
    display: flex;
    align-items: flex-start;
    gap: 0.6rem;
    margin: 0.75rem 0;
    animation: slideInLeft 0.2s ease;
}

.msg-avatar {
    width: 36px;
    height: 36px;
    border-radius: 50%;
    background: linear-gradient(135deg, #06b6d4, #0891b2);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1rem;
    flex-shrink: 0;
    box-shadow: 0 2px 10px rgba(6, 182, 212, 0.3);
}

.msg-assistant-bubble {
    max-width: 75%;
    background: rgba(30, 33, 48, 0.9);
    border: 1px solid rgba(124, 58, 237, 0.2);
    color: #e2e8f0;
    padding: 0.85rem 1.1rem;
    border-radius: 18px 18px 18px 4px;
    font-size: 0.9rem;
    line-height: 1.7;
    backdrop-filter: blur(10px);
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    word-wrap: break-word;
}

.msg-assistant-bubble.error {
    border-color: rgba(239, 68, 68, 0.4);
    background: rgba(239, 68, 68, 0.08);
}

/* Source badges */
.sources-row {
    display: flex;
    flex-wrap: wrap;
    gap: 0.35rem;
    margin-top: 0.6rem;
    padding-top: 0.5rem;
    border-top: 1px solid rgba(124, 58, 237, 0.15);
}

.source-badge {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    padding: 0.25rem 0.6rem;
    border-radius: 12px;
    background: rgba(6, 182, 212, 0.12);
    border: 1px solid rgba(6, 182, 212, 0.3);
    color: #22d3ee;
    font-size: 0.72rem;
    font-weight: 500;
}

/* ─── Typing indicator ──────────────────────────────────────────────────── */
.typing-indicator {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin: 0.5rem 0;
}

.typing-bubble {
    background: rgba(30, 33, 48, 0.9);
    border: 1px solid rgba(124, 58, 237, 0.2);
    border-radius: 18px 18px 18px 4px;
    padding: 0.85rem 1.1rem;
    display: flex;
    gap: 0.3rem;
    align-items: center;
}

.typing-dot {
    width: 8px;
    height: 8px;
    border-radius: 50%;
    background: #7c3aed;
    animation: bounce 1.2s infinite;
}

.typing-dot:nth-child(2) { animation-delay: 0.2s; }
.typing-dot:nth-child(3) { animation-delay: 0.4s; }

/* ─── Welcome / empty state ─────────────────────────────────────────────── */
.welcome-container {
    text-align: center;
    padding: 3rem 1rem;
    animation: fadeIn 0.4s ease;
}

.welcome-icon {
    font-size: 4rem;
    margin-bottom: 1rem;
    filter: drop-shadow(0 0 20px rgba(124, 58, 237, 0.5));
}

.welcome-title {
    font-size: 2rem;
    font-weight: 700;
    background: linear-gradient(90deg, #7c3aed, #06b6d4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.5rem;
}

.welcome-subtitle {
    color: #64748b;
    font-size: 1rem;
    margin-bottom: 2rem;
}

/* ─── Suggested prompt cards ────────────────────────────────────────────── */
.prompt-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 0.75rem;
    max-width: 700px;
    margin: 0 auto;
}

.prompt-card {
    background: rgba(30, 33, 48, 0.8);
    border: 1px solid rgba(124, 58, 237, 0.2);
    border-radius: 12px;
    padding: 0.9rem 1rem;
    cursor: pointer;
    transition: all 0.2s ease;
    text-align: left;
    backdrop-filter: blur(10px);
}

.prompt-card:hover {
    background: rgba(124, 58, 237, 0.15);
    border-color: rgba(124, 58, 237, 0.5);
    transform: translateY(-2px);
    box-shadow: 0 6px 20px rgba(124, 58, 237, 0.2);
}

.prompt-card-icon {
    font-size: 1.5rem;
    margin-bottom: 0.4rem;
}

.prompt-card-text {
    font-size: 0.82rem;
    color: #cbd5e1;
    font-weight: 500;
    line-height: 1.4;
}

/* ─── Status bar (sidebar bottom) ───────────────────────────────────────── */
.status-bar {
    padding: 0.75rem 1rem;
    border-radius: 10px;
    background: rgba(30, 33, 48, 0.6);
    border: 1px solid rgba(255,255,255,0.06);
    font-size: 0.78rem;
    color: #64748b;
    margin-top: auto;
}

.status-online {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    color: #34d399;
    font-weight: 500;
}

.status-offline {
    display: inline-flex;
    align-items: center;
    gap: 0.35rem;
    color: #f87171;
    font-weight: 500;
}

.status-dot {
    width: 7px;
    height: 7px;
    border-radius: 50%;
}

.status-dot.online {
    background: #34d399;
    box-shadow: 0 0 6px #34d399;
    animation: pulse 2s infinite;
}

.status-dot.offline {
    background: #f87171;
}

/* ─── Input area ────────────────────────────────────────────────────────── */
[data-testid="stChatInput"] {
    background: rgba(22, 27, 46, 0.95) !important;
    border: 1px solid rgba(124, 58, 237, 0.35) !important;
    border-radius: 16px !important;
    backdrop-filter: blur(10px);
}

[data-testid="stChatInput"]:focus-within {
    border-color: rgba(124, 58, 237, 0.7) !important;
    box-shadow: 0 0 0 3px rgba(124, 58, 237, 0.15) !important;
}

/* ─── Section labels (sidebar) ──────────────────────────────────────────── */
.sidebar-section-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #475569;
    margin: 1.2rem 0 0.5rem 0.25rem;
}

/* ─── Divider ───────────────────────────────────────────────────────────── */
.custom-divider {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.06);
    margin: 1rem 0;
}

/* ─── Animations ────────────────────────────────────────────────────────── */
@keyframes slideInRight {
    from { opacity: 0; transform: translateX(20px); }
    to   { opacity: 1; transform: translateX(0); }
}

@keyframes slideInLeft {
    from { opacity: 0; transform: translateX(-20px); }
    to   { opacity: 1; transform: translateX(0); }
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to   { opacity: 1; transform: translateY(0); }
}

@keyframes bounce {
    0%, 80%, 100% { transform: scale(0.6); opacity: 0.4; }
    40%           { transform: scale(1);   opacity: 1; }
}

@keyframes pulse {
    0%, 100% { box-shadow: 0 0 4px #34d399; }
    50%       { box-shadow: 0 0 10px #34d399; }
}

/* ─── Markdown inside bubbles ───────────────────────────────────────────── */
.msg-assistant-bubble p  { margin: 0 0 0.5em; }
.msg-assistant-bubble p:last-child { margin-bottom: 0; }
.msg-assistant-bubble ul, .msg-assistant-bubble ol {
    padding-left: 1.2em;
    margin: 0.4em 0;
}
.msg-assistant-bubble table {
    border-collapse: collapse;
    width: 100%;
    font-size: 0.85em;
    margin: 0.5em 0;
}
.msg-assistant-bubble th {
    background: rgba(124, 58, 237, 0.2);
    color: #c4b5fd;
    padding: 0.4em 0.8em;
    text-align: left;
    font-weight: 600;
}
.msg-assistant-bubble td {
    padding: 0.35em 0.8em;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    color: #cbd5e1;
}
.msg-assistant-bubble strong { color: #e2e8f0; }
.msg-assistant-bubble code {
    background: rgba(124,58,237,0.15);
    padding: 0.1em 0.35em;
    border-radius: 4px;
    font-size: 0.88em;
    color: #a78bfa;
}

/* ─── Session ID pill ───────────────────────────────────────────────────── */
.session-pill {
    display: inline-block;
    padding: 0.25rem 0.6rem;
    background: rgba(124, 58, 237, 0.1);
    border: 1px solid rgba(124, 58, 237, 0.2);
    border-radius: 20px;
    font-size: 0.7rem;
    color: #7c3aed;
    font-family: monospace;
    word-break: break-all;
}
"""


def inject_styles() -> None:
    """Inject all custom CSS into the Streamlit page."""
    st.markdown(f"<style>{_CSS}</style>", unsafe_allow_html=True)
