from dotenv import load_dotenv
from langchain_groq import ChatGroq

from config.settings import LLM_MODEL, GROQ_API_KEY

load_dotenv()


def get_llm():
    return ChatGroq(
        model=LLM_MODEL,
        api_key=GROQ_API_KEY,
        temperature=0,
    )


def get_structured_llm(schema):
    return get_llm().with_structured_output(schema)