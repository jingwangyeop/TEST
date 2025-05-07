import streamlit as st
from openai import OpenAI
import time

apikey = st.text_input("openai api key를 입력하세요 :", type = "password")

client = OpenAI(api_key=apikey)


if 'apikey' not in st.session_state:
    st.session_state.apikey = apikey

if apikey != "" :
  @st.cache_data
    def what(gg):

      gg = st.text_input("질문하세요:")
    
    
    
      response = client.chat.completions.create(
          model = "gpt-4o-mini",
          messages = [
              {"role": "system", "content": gg}
          ]
      )
      
    
      st.write(response.choices[0].message.content)
      
    
            
