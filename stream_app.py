import streamlit as st
st.write("Hello World why not?")

import time

# yield로 텍스트를 점점 반환하는 함수
def generate_text():
    yield "안녕하세요.\n"
    time.sleep(0.5)
    yield "이건 st.write_stream 예제입니다.\n"
    time.sleep(0.5)
    yield "점점 출력되는 텍스트죠?"

# st.write_stream()에 이 함수를 전달
st.write_stream(generate_text)
