from rag.ingest import load_documents, split_documents
from rag.cleaner import clean_documents
from rag.vectorstore import create_vectorstore

documents = load_documents()

documents = clean_documents(documents)

chunks = split_documents(documents)

from rag.ingest import load_documents, split_documents
from rag.cleaner import clean_documents
from rag.vectorstore import create_vectorstore

documents = load_documents()

documents = clean_documents(documents)

chunks = split_documents(documents)

# 👇 Add these two lines
print(f"Number of chunks: {len(chunks)}")
print(chunks[0].page_content[:300])

vectorstore = create_vectorstore(chunks)

print("FAISS Index Created Successfully!")
