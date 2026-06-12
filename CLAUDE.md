# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Monorepo for Thomas Guyader's CV, deployed as **three independent apps** that each build to their own `ghcr.io/tom333/*` image via a dedicated GitHub Actions workflow (triggered by path filter):

| Dir       | App                  | Image                  | Stack                                   |
|-----------|----------------------|------------------------|-----------------------------------------|
| `static/` | Static HTML CV       | `cv-static`            | nginx + Bootstrap, single `index.html`  |
| `src/`    | Dynamic CV generator | `dynamic-cv`           | Streamlit + CrewAI (multi-agent)        |
| `chat_bot/` | RAG chatbot        | `cv-chatbot`           | Chainlit + LangGraph + Qdrant + OpenAI  |

Deployment: Helm chart in `mycv/` (depends on the `qdrant` chart). Python 3.13, managed with `uv`.

## Commands

### Static CV (`static/`)
```bash
cd static && python -m http.server 9000   # local preview
```
Self-contained `index.html`: client-side PDF export (html2pdf.js) + Umami analytics, both via CDN.

### Dynamic CV (`src/`) — Streamlit + CrewAI
```bash
uv sync                                    # install deps (root pyproject.toml)
uv run streamlit run src/main.py           # run; needs OPENAI_API_KEY in .env
docker buildx build -t dynamic-cv .        # root Dockerfile builds this app
```
User pastes a job description in the sidebar → `CvCrew` (sequential crew of `researcher`, `profiler`, `resume_strategist`) regenerates a French markdown CV tailored to the posting.

### Chatbot (`chat_bot/`) — RAG over the CV
```bash
docker run -p 6333:6333 qdrant/qdrant      # or: kubectl port-forward svc/cv-qdrant 6333:6333 -n cv
python chat_bot/ingest_data.py             # embed chat_bot/data/*.md into Qdrant collection "cv" (run once)
chainlit run chat_bot/rag.py               # production chatbot; needs OPENAI_API_KEY + QDRANT_HOST
```

## Architecture notes

- **CrewAI config is YAML-driven**: agent roles/goals live in `src/config/agents.yaml`, task definitions in `src/config/tasks.yaml`. `src/crew.py` only wires them via `@agent`/`@task` decorators. Edit prompts/behavior in the YAML, not the Python. Source CV the agents read from is `src/data/CV.md`.

- **The chatbot has two parallel implementations** — know which one you're touching:
  - `chat_bot/rag.py` — **production** (what the Dockerfile runs). Chainlit UI + a `create_react_agent` with a single `search_cv` tool, `MemorySaver` checkpointer, French system prompt.
  - `chat_bot/app/` (`graph.py`, `nodes.py`, `tools.py`, run via `main.py`) — experimental **self-corrective RAG** LangGraph (agent → retrieve → grade_documents → generate/rewrite loop). Not wired into the Docker image.
  - Both embed/retrieve against the same Qdrant `"cv"` collection using `OpenAIEmbeddings`; the LLM is hardcoded to `gpt-4o-mini` throughout.

- **Hardcoded paths to fix if you touch the crew**: `src/tools/cv_reader.py` has an absolute `mdx="/home/moi/projets/perso/cv/src/data/CV.md"` (stale — real repo is `/data/projets/perso/cv`). `FileReadTool` uses relative `../data/CV.md`.

- **`docker-compose.yml` is broken**: references `build: ./chatbot` but the dir is `chat_bot`. Prefer the per-app Docker builds above.

## Secrets

All apps read `OPENAI_API_KEY` (and chatbot reads `QDRANT_HOST`) from env / `.env` (gitignored). Never commit keys.
