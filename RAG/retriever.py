from langchain_community.vectorstores import FAISS

from config import VECTORSTORE_DIR
from rag.embeddings import get_embedding_model


def load_vectorstore():
    """
    Load the saved FAISS vector database.
    """

    embeddings = get_embedding_model()

    return FAISS.load_local(
        str(VECTORSTORE_DIR),
        embeddings,
        allow_dangerous_deserialization=True
    )


def get_retriever(k=5):
    """
    Return a retriever for semantic search.
    """

    vectorstore = load_vectorstore()

    return vectorstore.as_retriever(
        search_kwargs={"k": k}
    )

def retrieve_context(query: str, k: int = 5):
    """
    Retrieve the most relevant document chunks for a query.
    """

    retriever = get_retriever(k)

    return retriever.invoke(query)