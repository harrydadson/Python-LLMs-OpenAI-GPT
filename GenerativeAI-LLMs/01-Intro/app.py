import os, openai
from dotenv import load_dotenv, dotenv_values, find_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

load_dotenv()
config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

prompt = "How old is the universe"
messages = [HumanMessage(content=prompt)]

llm_model = "gpt-3.5-turbo"
llm = OpenAI(temperature=0.7)
chat_model = ChatOpenAI(temperature=0.7)

print(llm.predict("What is the weather in WA DC"))
print("========")
print(chat_model.predict_messages(messages).content)
