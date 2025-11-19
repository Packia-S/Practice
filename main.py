from config import settings
from langchain_cohere import ChatCohere

llm = ChatCohere(cohere_api_key = settings.cohere_api_key)

response = llm.invoke("what is the capital of India")

print(response.content)