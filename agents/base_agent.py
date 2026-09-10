from abc import ABC, abstractmethod

from rag.llm import get_structured_llm
from rag.retriever import retrieve_context

from schemas.agent import AgentResult


class BaseAgent(ABC):
    """
    Base class for all AI agents.
    """

    def __init__(self):

        self.llm = get_structured_llm(self.OUTPUT_SCHEMA)

    @property
    @abstractmethod
    def QUERY(self):
        """
        Retrieval query.
        """
        pass

    @property
    @abstractmethod
    def PROMPT(self):
        """
        LangChain PromptTemplate.
        """
        pass

    @property
    @abstractmethod
    def OUTPUT_SCHEMA(self):
        """
        Pydantic schema returned by this agent.
        """
        pass

    def retrieve(self):

        return retrieve_context(
            self.QUERY,
            k=10
        )

    def build_context(self, docs):

        return "\n\n".join(
            doc.page_content
            for doc in docs
        )

    def run(self, docs=None):
        """
        Run the agent.

        If docs are supplied (LangGraph workflow),
        reuse them.

        Otherwise perform retrieval.
        """

        if docs is None:
            docs = self.retrieve()

        context = self.build_context(docs)

        messages = self.PROMPT.format_messages(
            context=context
        )

        response = self.llm.invoke(messages)

        return AgentResult(
            response=response,
            sources=docs,
        )