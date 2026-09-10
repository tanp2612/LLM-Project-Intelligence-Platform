from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import PDF_DIR, CHUNK_SIZE, CHUNK_OVERLAP


def load_documents():
    """
    Load all PDF documents from the configured PDF directory.
    """

    documents = []

    for pdf_file in PDF_DIR.glob("*.pdf"):
        loader = PyMuPDFLoader(str(pdf_file))
        documents.extend(loader.load())

    return documents


def split_documents(documents):
    """
    Split documents into smaller overlapping chunks.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    return splitter.split_documents(documents)