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
  vector_store = client.vector_stores.create(name="BUSAN")

  file_paths = [pdffile]

  file_streams = [open(path, "rb") for path in file_paths]

  file_batch = client.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id,
    files=file_streams
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
    ],
    tools=[{
      "type":"file_search",
      "vector_store_ids" :[vector_store.id],
      "max_num_results":3
    }]
  )
  st.write(response.output_text)
