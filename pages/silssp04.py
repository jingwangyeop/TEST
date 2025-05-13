import streamlit as st
from openai import OpenAI

apikey = st.session_state.api_key
client = OpenAI(api_key=apikey)

st.title("Jin's chatPDF bot")
pdf = st.file_uploader("PDF파일을 올려주세요")

# 초기화 (세션 상태에 저장)
if 'vector_store' not in st.session_state:
    st.session_state.vector_store = None
if 'pdffile' not in st.session_state:
    st.session_state.pdffile = None

if pdf is not None and st.session_state.vector_store is None:
    # 파일 업로드 및 벡터스토어 생성
    pdffile = client.files.create(file=pdf, purpose="user_data")
    vector_store = client.vector_stores.create(name="BUSAN")

    file_batch = client.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id,
        files=[pdf]
    )

    st.session_state.vector_store = vector_store
    st.session_state.pdffile = pdffile

prompt = st.text_input("PDF 내용에 대해 질문해주세요 :")

if prompt != "":
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
            "type": "file_search",
            "vector_store_ids": [st.session_state.vector_store.id],
            "max_num_results": 3
        }]
    )
    st.write(response.output_text)

    def delete():
        client.vector_stores.delete(st.session_state.vector_store.id)
        st.session_state.vector_store = None
        st.session_state.pdffile = None

    st.button("Delete Vector Store", on_click=delete)
