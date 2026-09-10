from rag.retriever import load_vectorstore

vectorstore = load_vectorstore()

query = "What is the project development objective?"

results = vectorstore.similarity_search(query, k=5)

for i, doc in enumerate(results, 1):
    print("=" * 80)
    print(f"Result {i}")
    print(doc.metadata)
    print(doc.page_content[:500])