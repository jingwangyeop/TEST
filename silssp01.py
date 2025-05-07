import streamlit as st
from openai import OpenAI
import time

apikey = st.text_input("openai api key를 입력하세요 :", type = "password")

client = OpenAI(api_key=apikey)


@st.cache_data
def what():
    # 사용자가 질문을 입력하는 부분
    gg = st.text_input("질문하세요:")
    
    if gg:  # 사용자가 입력한 질문이 있으면
        # OpenAI API로 응답 생성
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": gg}
            ]
        )
        
        # 응답을 화면에 표시
        st.write(response.choices[0].message.content)
    
    return gg  # 질문 값 반환


if apikey != "":
    # 사용자 질문 받기 및 처리
    what() 
            
