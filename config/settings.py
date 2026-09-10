from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

# Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data Directories
DATA_DIR = PROJECT_ROOT / "data"
PDF_DIR = DATA_DIR / "pdfs" / "P173373"

# Vector Database
VECTORSTORE_DIR = PROJECT_ROOT / "vectorstore"

# Models
EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"
LLM_MODEL = "llama-3.3-70b-versatile"

# API Keys
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Chunking
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200