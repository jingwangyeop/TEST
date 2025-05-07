
import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=apikey)

import streamlit as st

st.title("Jin's chat bot")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Accept user input
if prompt := st.chat_input("Say something"):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Add bot response (echo)
    st.session_state.messages.append({"role": "assistant", "content": prompt})
