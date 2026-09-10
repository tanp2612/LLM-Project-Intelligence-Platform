from rag.ingest import load_documents, split_documents
from rag.cleaner import clean_documents


documents = load_documents()
documents = clean_documents(documents)


print(f"Loaded {len(documents)} pages.")

chunks = split_documents(documents)

print(f"Created {len(chunks)} chunks.")

print("-" * 50)

for i in range(5):
    print(f"\n===== Chunk {i+1} =====")
    print(chunks[i].page_content[:300])