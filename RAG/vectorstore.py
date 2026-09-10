from langchain_community.vectorstores import FAISS

from config import VECTORSTORE_DIR
from rag.embeddings import get_embedding_model


def create_vectorstore(chunks):
    """
    Create a FAISS vector database.
    """

    embeddings = get_embedding_model()

    vectorstore = FAISS.from_documents(
        documents=chunks,
        embedding=embeddings
    )

    vectorstore.save_local(str(VECTORSTORE_DIR))

    return vectorstore