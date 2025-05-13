import streamlit as st
from openai import OpenAI
apikey = st.session_state.api_key
client = OpenAI(api_key=apikey)
import time


if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None
if 'pdffile' not in st.session_state:
    st.session_state.pdffile = None
if 'uploaded' not in st.session_state:
    st.session_state.uploaded = False  # 새 키 추가
   
st.title("Jin's chatPDF bot")
pdf = st.file_uploader("PDF파일을 올려주세요")


if st.session_state.pdffile == None and st.session_state.vector_store is None and st.session_state.uploaded == False :
  time.sleep(1)
  pdffile = client.files.create(
    file=pdf,
    purpose="user_data"
  )
  vector_store = client.vector_stores.create(name="silssp04")

  file_batch = client.vector_stores.file_batches.upload_and_poll(
    vector_store_id=vector_store.id,
    files=[pdf]
  )
  st.session_state.vector_store = vector_store
  st.session_state.pdffile = pdffile
  st.session_state.uploaded = True
def delete():
  if "vector_store" in st.session_state and st.session_state.vector_store is not None:
      client.vector_stores.delete(st.session_state.vector_store.id)
      st.session_state.vector_store = None
      client.files.delete(st.session_state.pdffile.id)
      st.session_state.uploaded = False
st.button("Delete PDF All", on_click=delete)



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
            "file_id": st.session_state.pdffile.id,
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
      "vector_store_ids" :[st.session_state.vector_store.id],
      "max_num_results":3
    }]
  )
  st.write(response.output_text)

