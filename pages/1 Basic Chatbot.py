import streamlit as st
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
import os

if "sessionMessages" not in st.session_state:
    st.session_state.sessionMessages=[
        SystemMessage(content="You are a helpful assistance")
    ]

load_dotenv()

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.header("# Welcome to Streamlit! 👋")

user_input=st.text_input("You: ")
submit=st.button("Generate")

load_dotenv()

llm=ChatOpenAI(temperature=0)

if submit:
    st.session_state.sessionMessages.append(HumanMessage(content=user_input))
    llm_response=llm.invoke(st.session_state.sessionMessages)
    st.session_state.sessionMessages.append(AIMessage(content=llm_response.content))
    st.subheader("Answer:")
    st.write(llm_response.content)
    