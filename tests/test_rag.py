from pathlib import Path

from rag.rag_chain import ask_question

response = ask_question(
    "What is the project development objective?"
)

print("\nANSWER\n")
print(response["answer"])

print("\nSOURCES\n")

for doc in response["sources"]:
    filename = Path(doc.metadata["source"]).name
    page = doc.metadata["page"]

    print(f"{filename} | Page {page}")