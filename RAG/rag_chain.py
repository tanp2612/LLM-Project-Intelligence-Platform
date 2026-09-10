from rag.retriever import get_retriever
from rag.llm import get_llm
from langchain_core.prompts import ChatPromptTemplate

retriever = get_retriever()
llm = get_llm()

PROMPT = ChatPromptTemplate.from_template(
"""
You are an AI Project Intelligence Assistant.

Use ONLY the information provided in the context.

If the answer cannot be found in the context,
say exactly:

"I couldn't find this information in the project documents."

Keep answers concise, factual and professional.

Context:
{context}

Question:
{question}
"""
)


def ask_question(question: str):

    docs = retriever.invoke(question)

    context = "\n\n".join(
        doc.page_content
        for doc in docs
    )

    messages = PROMPT.format_messages(
        context=context,
        question=question,
    )

    response = llm.invoke(messages)

    return {
    "answer": response.content,
    "sources": docs
    }
