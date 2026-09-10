🧠 Project Intelligence Platform

Multi-Agent RAG System for World Bank Project Intelligence

The Sparks Foundation — Data Science Intern Project

A production-oriented Multi-Agent Retrieval-Augmented Generation (RAG) platform designed to answer questions from World Bank project documentation using semantic retrieval, specialized AI agents, workflow orchestration, and source-grounded generation.

🚀 Overview

The Project Intelligence Platform transforms large collections of World Bank project documents into an interactive question-answering system.

The platform processes documents such as:

📄 Project Appraisal Documents (PAD)

📊 Implementation Status & Results Reports (ISR)

🛡️ Environmental and Social Framework (ESF) documents

📑 Implementation Completion & Results Reports (ICR)

Instead of relying solely on an LLM's pretrained knowledge, the system retrieves relevant document context first and then generates answers grounded in that evidence.

Key Capabilities

🔎 Semantic search across 500+ document chunks

🤖 Multi-agent question routing

🧩 LangGraph-based workflow orchestration

📚 FAISS vector search

🧠 BGE-based text embeddings

⚡ Llama 3.1 inference through the Groq API

🏷️ Metadata-aware retrieval

🎯 Top-K context selection

✍️ Prompt-engineered generation

🛡️ Context validation and hallucination reduction

📌 Source-grounded responses with citations

🏗️ System Architecture

The platform follows a modular 8-layer architecture designed for separation of concerns, maintainability, and extensibility.

┌───────────────────────────────────────────────┐
│                    UI Layer                   │
│        User Query / Response Interface        │
├───────────────────────────────────────────────┤
│              Orchestration Layer              │
│             LangGraph Workflow                │
├───────────────────────────────────────────────┤
│                  Agent Layer                  │
│ Knowledge │ Risk │ Summary │ Health Agents   │
├───────────────────────────────────────────────┤
│                   Tool Layer                  │
│       Retrieval / Processing Utilities        │
├───────────────────────────────────────────────┤
│                Retrieval Layer                │
│ Metadata Filter → Embedding Search → Top-K   │
├───────────────────────────────────────────────┤
│              Knowledge Base Layer             │
│        Documents → Chunks → FAISS Index       │
├───────────────────────────────────────────────┤
│                    LLM Layer                  │
│           Llama 3.1 via Groq API              │
├───────────────────────────────────────────────┤
│                 Guardrails Layer              │
│       Context Validation / Grounding          │
└───────────────────────────────────────────────┘

🤖 Multi-Agent Workflow

The system uses four specialized agents, coordinated through a LangGraph workflow.

Agent

Responsibility

🔍 Knowledge Agent

Retrieves and answers factual questions from project documentation

⚠️ Risk Agent

Identifies and summarizes project-related risks and concerns

📝 Summary Agent

Produces concise summaries of relevant project information

❤️ Health Agent

Analyzes project health/status information using retrieved evidence

High-Level Flow

User Query
    │
    ▼
Query Understanding
    │
    ▼
LangGraph Orchestration
    │
    ├──────────────┬──────────────┬──────────────┐
    ▼              ▼              ▼              ▼
Knowledge       Risk           Summary        Health
 Agent          Agent           Agent          Agent
    │              │              │              │
    └──────────────┴──────────────┴──────────────┘
                       │
                       ▼
              Retrieval Pipeline
                       │
                       ▼
                Context Validation
                       │
                       ▼
             Llama 3.1 Generation
                       │
                       ▼
              Grounded Response
                + Citations

🔎 Retrieval-Augmented Generation Pipeline

The retrieval pipeline is designed to provide relevant evidence to the LLM before generation.

1. Document Processing

World Bank project documents are collected and prepared for downstream retrieval.

Raw Documents
      ↓
Document Parsing
      ↓
Text Cleaning
      ↓
Chunking
      ↓
Metadata Assignment

2. Embedding Generation

Document chunks are transformed into dense vector representations using BGE embeddings.

Text Chunk
    ↓
BGE Embedding Model
    ↓
Dense Vector

3. Vector Indexing

The generated embeddings are stored in a FAISS vector index, enabling efficient similarity-based retrieval.

4. Query Retrieval

For an incoming question:

User Query
    ↓
Query Embedding
    ↓
Metadata Filtering
    ↓
FAISS Similarity Search
    ↓
Top-K Relevant Chunks

5. Grounded Generation

Retrieved context is passed to the LLM through structured prompts.

User Query
    +
Retrieved Context
    +
Prompt Instructions
        ↓
   Llama 3.1
        ↓
Validated, Source-Grounded Answer

This architecture helps reduce unsupported responses by requiring the generation stage to work from retrieved project evidence.

🧠 Technologies & Tools

Category

Technology

Language

Python

LLM

Llama 3.1

LLM Inference

Groq API

RAG Framework

LangChain

Agent Orchestration

LangGraph

Vector Database / Search

FAISS

Embeddings

BGE

Prompting

Prompt Engineering

Architecture

Modular Multi-Agent RAG

Version Control

Git / GitHub

📂 Project Structure

project-intelligence-platform/
│
├── RAG/                    # Retrieval-Augmented Generation components
├── agents/                 # Specialized AI agents
├── config/                 # Configuration and environment settings
├── conversation/           # Conversation / dialogue management
├── data/                   # Source and processed project data
├── docs/                   # Documentation and project resources
├── graph/                  # LangGraph workflow definitions
├── memory/                 # Agent / conversation memory components
├── schemas/                # Data models and structured schemas
├── tests/                  # Testing suite
├── vectorstore/            # FAISS vector index and retrieval assets
│
├── app.py                  # Application entry point
├── main.py                 # Main execution / orchestration
├── requirements.txt        # Python dependencies
├── .gitignore
└── README.md

⚙️ Installation & Setup

Prerequisites

Python 3.9+

Git

A valid Groq API key

1. Clone the Repository

git clone https://github.com/tanp2612/LLM-Project-Intelligence-Platform.git
cd LLM-Project-Intelligence-Platform

2. Create a Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate

macOS / Linux

python3 -m venv venv
source venv/bin/activate

3. Install Dependencies

pip install -r requirements.txt

4. Configure Environment Variables

Create a .env file and add your API credentials:

GROQ_API_KEY=your_groq_api_key

⚠️ Never commit API keys or other credentials to GitHub.

5. Run the Application

python app.py

If your project uses main.py as the primary entry point:

python main.py

💡 Example Use Cases

The platform can support questions such as:

Knowledge: What are the key objectives of this World Bank project?

Risk: What major risks are identified in the project documentation?

Summary: Summarize the project's implementation progress.

Health: What does the available documentation indicate about the current project status?

The system retrieves relevant evidence before generating the response rather than answering solely from the LLM's internal knowledge.

🎯 Engineering Highlights

Semantic Retrieval

Uses dense vector embeddings and FAISS similarity search to retrieve conceptually relevant content instead of relying only on keyword matching.

Metadata-Aware Search

Metadata filtering narrows the search space and helps retrieve context from the appropriate document or project category.

Multi-Agent Architecture

Different analytical responsibilities are separated into specialized agents, making the system easier to extend and maintain.

Graph-Based Orchestration

LangGraph provides explicit workflow control between query processing, agent execution, retrieval, validation, and response generation.

Prompt Engineering

Structured prompts guide the LLM toward concise, context-aware, and evidence-based responses.

Grounding & Guardrails

Retrieved context is validated before generation to reduce unsupported claims and improve response reliability.

📈 Key Project Outcomes

Built a modular Multi-Agent RAG architecture

Indexed and searched 500+ document chunks

Integrated Llama 3.1 with Groq API for LLM inference

Implemented BGE embeddings + FAISS for semantic retrieval

Developed 4 specialized AI agents

Added metadata filtering and Top-K retrieval

Designed source-grounded response generation with validation and citations

Structured the application into 8 independent architectural layers

🔮 Future Enhancements

Potential extensions include:

📊 Retrieval and generation evaluation dashboards

🔁 Automated document ingestion pipelines

🧪 RAG evaluation using metrics such as context relevance and answer faithfulness

💾 Persistent conversational memory

🔐 Role-based access control

📈 Observability and agent-level performance monitoring

⚡ Retrieval and inference latency optimization

🌐 Deployment as a scalable cloud application

👩‍💻 Internship

The Sparks Foundation — Data Science Intern

Project: Project Intelligence Platform — Multi-Agent RAG System

This project demonstrates practical application of Generative AI, Retrieval-Augmented Generation, semantic search, LLM orchestration, vector databases, and multi-agent systems to a real-world document intelligence problem.

🛠️ Core Skills Demonstrated

Python RAG LLMs LangChain LangGraph FAISS BGE Embeddings Prompt Engineering Semantic Search Multi-Agent Systems Vector Search NLP API Integration AI Architecture

📜 License

This repository is intended for educational and portfolio purposes. Please ensure that any source documents and datasets used comply with their respective usage and licensing requirements.
