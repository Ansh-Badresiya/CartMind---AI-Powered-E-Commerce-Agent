# ShopBot AI — Streamlit UI

A modern, dark-themed chat interface for the **E-commerce AI Agent** (FastAPI + LangGraph).

## Features

- 💬 **Real-time chat** with the AI agent
- 🔍 **Q&A** — ask about products (RAG-powered semantic search)
- 🛒 **Order placement** with Human-in-the-Loop confirmation step
- 📦 **Order tracking** by session
- 🧭 **Sidebar** with category quick-filters and live API status
- ✨ **Suggested prompts** on the welcome screen
- 🎨 **Dark glassmorphism** theme with smooth animations

## Quick Start

### Option A — Run locally (FastAPI already running)

```bash
# Install UI deps
pip install -r ui/requirements.txt

# Run (FastAPI must be on http://localhost:8000)
streamlit run streamlit_app.py
```

Open **http://localhost:8501**

### Option B — Run via Docker Compose (full stack)

```bash
# Build everything including the UI service
docker compose build

# Start all services (API + ChromaDB + Streamlit UI)
docker compose up -d

# Build the vector index (first time only)
docker compose run --rm ecommerce-agent python -m embedding.index
```

| Service     | URL                        |
|-------------|----------------------------|
| Streamlit UI | http://localhost:8501      |
| FastAPI      | http://localhost:8000      |
| Swagger docs | http://localhost:8000/docs |
| ChromaDB     | http://localhost:8001      |

## Project Structure

```
ui/
├── __init__.py
├── config.py          # All constants — API URL, categories, prompts
├── api_client.py      # Typed HTTP client for the FastAPI backend
├── session.py         # Centralised st.session_state management
├── styles.py          # All custom CSS (dark theme, animations)
├── requirements.txt   # UI-only dependencies
└── components/
    ├── __init__.py
    ├── sidebar.py     # Logo, new chat, category filters, status
    ├── chat.py        # Message bubbles, welcome screen, typing indicator
    └── header.py      # Top bar with turn counter

streamlit_app.py       # Entry point — page config + layout orchestration
Dockerfile.ui          # Minimal Docker image for the UI service
.streamlit/
└── config.toml        # Streamlit theme (dark purple/slate)
```

## Environment Variables

| Variable        | Default                    | Description                      |
|----------------|----------------------------|----------------------------------|
| `AGENT_API_URL` | `http://localhost:8000`    | FastAPI backend base URL         |
