import streamlit as st
from openai import OpenAI
apikey = st.session_state.api_key
client = OpenAI(api_key=apikey)


st.title("Jin's chatPDF bot")
pdf = st.file_uploader("PDF파일을 올려주세요")

