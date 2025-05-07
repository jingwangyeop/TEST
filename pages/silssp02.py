
import streamlit as st
from openai import OpenAI
apikey = st.session_state.api_key
client = OpenAI(api_key=apikey)


st.title("Jin's chat bot")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if ppt := st.chat_input("Ask a question to the latest AI. If you want to stop chatting, type 'stop':"):
     response = client.responses.create(
        model="gpt-4.1-mini",
        input=ppt
    )
     st.session_state.messages.append({"role": "user", "content": ppt})
     st.session_state.messages.append({"role": "AI", "content": response.output[0].content[0].text})
    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
