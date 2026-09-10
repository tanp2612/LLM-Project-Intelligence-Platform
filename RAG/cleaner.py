import re

from langchain_core.documents import Document


def clean_text(text: str) -> str:
    """
    Clean extracted PDF text before chunking.
    """

    # Remove World Bank internal OPS markers
    text = re.sub(r"@#&OPS.*?(?=\n)", "", text)

    # Remove repeated disclosure text
    text = re.sub(r"Public Disclosure Authorized", "", text)

    # Collapse multiple blank lines
    text = re.sub(r"\n\s*\n+", "\n\n", text)

    # Collapse multiple spaces
    text = re.sub(r"[ \t]+", " ", text)

    # Remove repeated page headers
    text = re.sub(r"The World Bank", "", text)

    # Remove confidentiality labels
    text = re.sub(r"Official Use Only", "", text)

    # Remove page numbers
    text = re.sub(r"Page\s+\d+", "", text)

    return text.strip()


def clean_documents(documents):
    """
    Apply text cleaning to all loaded documents.
    """

    cleaned = []

    for doc in documents:
        cleaned_doc = Document(
            page_content=clean_text(doc.page_content),
            metadata=doc.metadata
        )

        cleaned.append(cleaned_doc)

    return cleaned