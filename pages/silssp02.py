
import streamlit as st
from openai import OpenAI
apikey = st.session_state.api_key
client = OpenAI(api_key=apikey)


st.title("Jin's chat bot")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history

while True :
    if ppt := st.chat_input("최근에나온 AI에게 질문을 해보세요. 채팅을 멈추고싶으면 '그만'을 치세요.:"):
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=ppt
        )
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.session_state.messages.append({"role": "AI", "content": response.output[0].content[0].text})
    if ppt == '그만' :
        break
    for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

