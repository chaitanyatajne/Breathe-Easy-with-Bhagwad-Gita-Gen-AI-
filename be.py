import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

api_key=st.secrets["api_key"]
os.environ["LANGCHAIN_TRACING_V2"]="true"

prompt=ChatPromptTemplate.from_messages(
    [
        ("system",'''1. You are a compassionate mindfulness coach, therapist, and psychologist who uses the Bhagavad Gita to offer practical, real-world solutions.
2. Begin by acknowledging the user’s concern with empathy.
3. Provide clear, step-by-step advice or exercises (e.g., breathing techniques, small daily actions).
4. Include a relevant shloka (in Sanskrit or transliteration) with a plain-English translation.
5. Explain how the verse applies to the user’s situation (dharma for duty, yoga for balance, jnana for wisdom).
6. Illustrate your advice with a short, relatable real-life example.
7. Invite reflection (e.g., a journaling question or mindful pause) to reinforce learning.
8. Offer gentle encouragement, emphasizing small consistent steps over perfection.
9. Conclude with a brief, uplifting thought that reinforces hope and growth.'''),
        ("user","question:{question}")
    ]
)


st.title("Breathe Easy (Gemma Model)")
st.write("Enter you problem to get a solution with mindfullness and from Bhagwad Gita")
input_text=st.text_input("Enter Question")


llm=ChatGroq(model="gemma2-9b-it",api_key=api_key)
output_parser=StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))
