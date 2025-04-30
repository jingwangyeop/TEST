import streamlit as st
!pip install openai
import openai
from openai import OpenAI


apikey = st.text_input("입력해라 :")

client = OpenAI(api_key=apikey)

response = client.chat.completions.create(
    model = "gpt-4.1-mini",
    messages = [
        {"role": "system", "content": "You are a helpful chat bot"}
    ]
)

st.write(response.choices[0].message.content)
