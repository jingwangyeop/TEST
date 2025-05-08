import streamlit as st
from openai import OpenAI
apikey = st.session_state.api_key
client = OpenAI(api_key=apikey)


st.title("Jin's chatPDF bot")
pdf = st.file_uploader("PDF파일을 올려주세요")
st.write(type(pdf))
"""
if pdf !=null :
  prompt = st.text.input("PDF 내용에 대해 질문해주세요 :")

if prompt !="":
  response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
      {
        "role": "user",
        "content": [
          {
            "type": "input_file",
            "file_id": pdf.id,
          },
          {
            "type": "input_text",
            "text": prompt,
          },
        ]
      }
    ]
  )
"""
