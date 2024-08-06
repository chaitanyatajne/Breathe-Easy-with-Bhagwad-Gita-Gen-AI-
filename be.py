import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

api_key="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"
os.environ["LANGCHAIN_TRACING_V2"]="true"

prompt=ChatPromptTemplate.from_messages(
    [
        ("system","consider yourself as a mindfullness coach and a psychologist who helps people in their day to day life by answering their questions with detailed and real world solutions based on bhagwad gita and also provide the shlokas or quotes from bhagwad gita to them."),
        ("user","question:{question}")
    ]
)


st.title("Breathe Easy (Gemma Model)")
st.write("Enter you problem to get a solution with mindfullness and from Bhagwad Gita")
input_text=st.text_input("Enter Question")


llm=ChatGroq(model="Gemma2-9b-It",api_key=api_key)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
