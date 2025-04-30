import streamlit as st
from openai import OpenAI
import time

apikey = st.text_input("입력해라 :")

client = OpenAI(api_key=apikey)


time.sleep(2)

gg = st.text_input("말해라 :")

time.sleep(1)

response = client.chat.completions.create(
    model = "gpt-4o-mini",
    messages = [
        {"role": "system", "content": gg}
    ]
)


st.write(response.choices[0].message.content)


