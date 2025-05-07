import streamlit as st
from openai import OpenAI
import time

apikey = st.text_input("openai api key를 입력하세요 :", type = "password")

client = OpenAI(api_key=apikey)


@st.cache_data
def what():
    if apikey != "":
        gg = st.text_input("질문하세요:")
    
        if gg:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": gg}
                ]
            )
    
            that = st.write(response.choices[0].message.content)
        return that

what()
