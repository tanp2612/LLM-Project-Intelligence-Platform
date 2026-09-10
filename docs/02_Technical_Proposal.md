# Technical Proposal v1.0

## Objective

Develop an AI-powered Project Intelligence Platform that enables users to query and analyze World Bank project documents using Retrieval-Augmented Generation (RAG).

---

## Technology Stack

| Component       | Selection              |
| --------------- | ---------------------- |
| LLM             | Llama 3.1 70B (Groq)   |
| Framework       | LangChain              |
| UI              | Streamlit              |
| Embedding Model | BAAI/bge-small-en-v1.5 |
| Vector Database | FAISS                  |
| PDF Processing  | PyMuPDF                |

---

## Core Features

* Intelligent Project Knowledge Assistant
* Executive Summary Generator
* Risk Analysis Agent


---

## Design Rationale

* **BAAI/bge-small-en-v1.5** — Free, lightweight, and provides strong semantic retrieval performance.
* **FAISS** — Local vector database for fast similarity search and easy setup.
* **Modular Python Agents** — Sufficient for the MVP; LangGraph can be introduced in future iterations if advanced orchestration is required.
* **Preloaded Documents** — Ensures a stable, fast, and reliable demonstration without runtime document indexing.

---


## Planned Scope (MVP)

* RAG-based document search
* Executive summary generation
* Project risk analysis
* Streamlit-based interactive interface

---

# Project Structure v1.0

```text
AI-Project-Intelligence/
│
├── app.py                      # Streamlit application
│
├── agents/                     # AI agents
│   ├── risk_agent.py
│   └── summary_agent.py
│
├── rag/                        # RAG pipeline
│   ├── ingest.py
│   ├── embeddings.py
│   ├── retriever.py
│   └── vectorstore.py
│
├── prompts/                    # Prompt templates
│
├── data/
│   └── pdfs/                   # World Bank project documents
│
├── vectorstore/                # FAISS index
│
├── docs/                       # Project documentation
│   ├── 01_Architecture.md
│   ├── 02_Technical_Decisions.md
│   ├── 03_Demo_Script.md
│   └── 04_Future_Roadmap.md
│
├── assets/
│   ├── diagrams/
│   └── screenshots/
│
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

## Design Principles

* Modular and maintainable architecture.
* Single responsibility for each module.
* Clear separation between UI, RAG pipeline, AI agents, documentation, and assets.
* Designed for easy extension with additional agents, deployment tools, and cloud services in future versions.

---

**Goal:** Deliver a working, demo-ready MVP within the project timeline while keeping the architecture modular and extensible.
