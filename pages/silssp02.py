import streamlit as st
from openai import OpenAI

apikey = st.text_input("OPENAI API KEY를 입력하세요 :", type = "password")
client = OpenAI(api_key=apikey)

