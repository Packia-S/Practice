from config import settings
from langchain_cohere import ChatCohere
from pydantic import BaseModel

class Country(BaseModel):
    name: str
    capital: str

llm = ChatCohere(cohere_api_key=settings.cohere_api_key)

# Correct method name
structured_llm = llm.with_structured_output(Country)

response = structured_llm.invoke("What is the capital of India?")

print(response)