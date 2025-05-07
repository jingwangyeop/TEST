import streamlit as st
from openai import OpenAI

apikey = st.text_input("OPENAI API KEY를 입력하세요 :", type = "password")
client = OpenAI(api_key=apikey)

st.chat_input(placeholder="Your message", *, key=None, max_chars=None, accept_file=False, file_type=None, disabled=False, on_submit=None, args=None, kwargs=None)
