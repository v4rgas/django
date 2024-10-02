from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'))

print(llm.invoke("What is the capital of the United States?"))