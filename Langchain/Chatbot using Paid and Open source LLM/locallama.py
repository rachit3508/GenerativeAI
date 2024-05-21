from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import ollama

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"


#Define Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("user","You are a helpfull assistant. Please respond to the user query"),
        ("user","Question:{question}")
    ]
)

# Streamlit framework
st.title("Langchain Demo with Open API")
input_text = st.text_input("Search the Topic you want.")

#Before using any model you have to download the model first.
#1. open powershell
#2. ollama run model_name
#3. it will download the model and than you can use it in your code

llm = ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))