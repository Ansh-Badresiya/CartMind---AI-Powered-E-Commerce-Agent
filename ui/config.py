"""
ui/config.py
------------
Central configuration for the Streamlit UI.
All constants live here — no magic strings scattered across modules.
"""

from __future__ import annotations

import os

# ---------------------------------------------------------------------------
# API
# ---------------------------------------------------------------------------
API_BASE_URL: str = os.getenv("AGENT_API_URL", "http://localhost:8000")
API_CHAT_ENDPOINT: str = f"{API_BASE_URL}/chat"
API_TIMEOUT_SECONDS: int = 60

# ---------------------------------------------------------------------------
# Page metadata
# ---------------------------------------------------------------------------
PAGE_TITLE: str = "ShopBot AI"
PAGE_ICON: str = "🛒"
PAGE_LAYOUT: str = "wide"

# ---------------------------------------------------------------------------
# Chat UX
# ---------------------------------------------------------------------------
MAX_HISTORY_DISPLAY: int = 100        # max messages shown in viewport
WELCOME_MESSAGE: str = (
    "👋 Hi! I'm **ShopBot AI** — your personal e-commerce assistant.\n\n"
    "I can help you with:\n"
    "- 🔍 **Product questions** — specs, prices, availability\n"
    "- 🛒 **Placing orders** — just tell me what you want to buy\n"
    "- 📦 **Order tracking** — ask me where your order is\n\n"
    "What can I help you with today?"
)

# ---------------------------------------------------------------------------
# Suggested prompts shown on empty chat
# ---------------------------------------------------------------------------
SUGGESTED_PROMPTS: list[dict[str, str]] = [
    {"icon": "💻", "label": "Tell me about laptops"},
    {"icon": "🎮", "label": "What gaming accessories do you have?"},
    {"icon": "🎧", "label": "Show me wireless headphones"},
    {"icon": "🛒", "label": "I want to buy a ProBook 15"},
    {"icon": "📦", "label": "Where is my order?"},
    {"icon": "📱", "label": "Compare your phones"},
]

# ---------------------------------------------------------------------------
# Product catalog categories (for sidebar quick-filter chips)
# ---------------------------------------------------------------------------
PRODUCT_CATEGORIES: list[dict[str, str]] = [
    {"icon": "💻", "label": "Laptops"},
    {"icon": "📱", "label": "Phones"},
    {"icon": "🎧", "label": "Audio"},
    {"icon": "🖥️", "label": "Monitors"},
    {"icon": "⌨️", "label": "Accessories"},
    {"icon": "⌚", "label": "Wearables"},
    {"icon": "📦", "label": "Storage"},
    {"icon": "🌐", "label": "Networking"},
    {"icon": "📐", "label": "Tablets"},
]
