from langchain_core.prompts import ChatPromptTemplate
from rag.llm import get_llm


class ChatAgent:

    def __init__(self):

        self.llm = get_llm()

    def run(
        self,
        messages,
        docs,
    ):

        context = "\n\n".join(
            doc.page_content for doc in docs
        )

        system_prompt = f"""
You are an AI Project Intelligence Assistant.

Answer ONLY from the provided project documents.

Project Context:

{context}
"""

        response = self.llm.invoke(

            [

                ("system", system_prompt),

                *messages,

            ]

        )

        return response