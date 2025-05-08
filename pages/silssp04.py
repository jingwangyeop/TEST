import streamlit as st
from openai import OpenAI
apikey = st.session_state.api_key
client = OpenAI(api_key=apikey)


st.title("Jin's chatPDF bot")
pdf = st.file_uploader("PDF파일을 올려주세요")


if pdf !=None :
  pdffile = client.files.create(
    file=pdf,
    purpose="user_data"
  )
  prompt = st.text_input("PDF 내용에 대해 질문해주세요 :")

if prompt !="":
  response = client.responses.create(
    model="gpt-4.1-mini",
    input=[
      {
        "role": "user",
        "content": [
          {
            "type": "input_file",
            "file_id": pdffile.id,
          },
          {
            "type": "input_text",
            "text": prompt,
          },
        ]
      }
    ]
  )
  st.write(response.output_text)
