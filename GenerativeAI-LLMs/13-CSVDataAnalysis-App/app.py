import streamlit as st
import openai
from dotenv import load_dotenv, dotenv_values
from utils import query_agent

load_dotenv()
config = dotenv_values(".env")
apikey = openai.api_key = config["OPENAI_API_KEY"]
#HuggingFaceHub_api_key = config["HUGGINGFACEHUB_API_TOKEN"]

st.title("Let's do some analysis on your CSV")
st.header("Please upload your CSV file here:")

# Capture the CSV file
data = st.file_uploader("Upload CSV file",type="csv")

query = st.text_area("Enter your query")
button = st.button("Generate Response")

if button:
    # Get Response
    answer =  query_agent(data,query)
    st.write(answer)