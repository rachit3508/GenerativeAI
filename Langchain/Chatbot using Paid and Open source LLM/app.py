from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
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

#OpenAI LLM
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({'question':input_text}))


