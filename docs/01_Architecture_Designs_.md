# AI Project Intelligence Platform

## Objective

Build an enterprise AI assistant that enables users to interact with World Bank project documents using natural language.

---

## Core Features

* Intelligent Project Knowledge Assistant
* Executive Summary Generator
* Risk Analysis Agent

---

## Tech Stack

* Python
* Streamlit
* LangChain
* Groq API
* Llama 3.1 70B
* FAISS
* BAAI `bge-small-en-v1.5`
* PyMuPDF

---

# 🏗️ Overall Architecture

### Purpose

* Provides a high-level view of the entire application.
* Shows how user requests travel through the system.
* Highlights the interaction between the UI, RAG pipeline, LLM, and AI agents.
* Serves as the foundation for the remaining architecture diagrams.

### Components Covered

* User
* Streamlit UI
* Application Controller
* Retriever
* Summary Agent
* Risk Agent
* Llama 3.1 70B (Groq)
* FAISS Vector Database
* Embedding Model
* PDF Ingestion Pipeline
* World Bank Project Documents

---
> **Overall System Architecture**

![Overall Architecture](../assets/diagrams/architecture.png)

                           👤 User
                              │
                              ▼
                    ┌────────────────────┐
                    │    Streamlit UI    │
                    └────────────────────┘
                              │
                              ▼
                    ┌────────────────────┐
                    │ Application Control│
                    └────────────────────┘
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
    Chat Query         Summary Agent       Risk Agent
          │                   │                   │
          └──────────────┬────┴───────────────────┘
                         ▼
                  ┌───────────────┐
                  │   Retriever   │
                  └───────────────┘
                         │
                         ▼
                  ┌───────────────┐
                  │     FAISS     │
                  └───────────────┘
                         ▲
                         │
                  Stored Embeddings
                         ▲
                         │
                  BGE Embeddings
                         ▲
                         │
                  Chunked Documents
                         ▲
                         │
                  PDF Ingestion
                         ▲
                         │
                 World Bank PDFs

                         │
           Retrieved Chunks
                         ▼
                  ┌───────────────┐
                  │ Prompt Builder│
                  └───────────────┘
                         │
                         ▼
          ┌─────────────────────────────┐
          │ Llama 3.1 70B (via Groq API)│
          └─────────────────────────────┘
                         │
                         ▼
                      Response

# 🔍 Retrieval-Augmented Generation (RAG) Pipeline

### Purpose

* Enables the LLM to answer questions using project-specific documents.
* Reduces hallucinations by grounding responses in retrieved context.
* Retrieves only the most relevant document chunks instead of processing entire PDFs.
* Forms the core intelligence layer of the application.

### Pipeline Stages

* PDF Ingestion
* Text Extraction
* Document Chunking
* Embedding Generation
* FAISS Vector Indexing
* Semantic Retrieval
* Prompt Construction
* Llama 3.1 70B (Groq)
* Grounded Response Generation

### Key Components

* **PyMuPDF** – Extracts text from PDF documents.
* **BAAI bge-small-en-v1.5** – Converts text chunks into vector embeddings.
* **FAISS** – Stores embeddings and performs similarity search.
* **Retriever** – Fetches the most relevant document chunks.
* **Llama 3.1 70B (Groq)** – Generates answers using the retrieved context.

### Outcome

* Context-aware responses
* Source-grounded answers
* Faster retrieval
* Improved response accuracy

---

> **RAG Pipeline Diagram**

![RAG Pipeline](../assets/diagrams/rag_pipeline.png)

                    📄 World Bank PDFs
                           │
                           ▼
                 ┌──────────────────┐
                 │  PDF Ingestion   │
                 │    (PyMuPDF)     │
                 └──────────────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │ Text Extraction  │
                 └──────────────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │ Document Chunking│
                 └──────────────────┘
                           │
                           ▼
                 ┌─────────────────────────┐
                 │ BGE Embedding Model      │
                 │ (bge-small-en-v1.5)      │
                 └─────────────────────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │  FAISS Vector DB │
                 └──────────────────┘
                           ▲
                           │
         Query Embedding   │
                           │
                    ┌──────────────────┐
                    │  User Question   │
                    └──────────────────┘
                           │
                           ▼
                 ┌─────────────────────────┐
                 │ BGE Embedding Model      │
                 │ (Query Embedding)        │
                 └─────────────────────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │ Similarity Search│
                 └──────────────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │ Top-K Chunks     │
                 └──────────────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │ Prompt Builder   │
                 └──────────────────┘
                           │
                           ▼
            ┌────────────────────────────┐
            │ Llama 3.1 70B (via Groq)   │
            └────────────────────────────┘
                           │
                           ▼
                 ┌──────────────────┐
                 │ Grounded Answer  │
                 └──────────────────┘
