import streamlit as st
import random,time

from urllib.error import URLError
import os,sys
module_path = ".."
sys.path.append(os.path.abspath(module_path))
from orchestrator.Orchestrator import Orchestrator

orchestrator=Orchestrator()

st.set_page_config(page_title="Chat with assistant", page_icon="💬")

st.markdown("# Chat with assistant")
st.sidebar.header("Chat with assistant")
st.write(
    """
    This time you can engage with a chat bot to keep the conversation as context
"""
)

if 'memory' not in st.session_state: #see if the memory hasn't been created yet
    st.session_state.memory = orchestrator.get_memory()

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

#st.session_state.messages.append({"role": "assistant", "content": "Hello, how can I help you?"})    
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


if query := st.chat_input(placeholder="Your message"):
    with st.chat_message("user"):
        st.markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})    

    response = f"Echo: {query}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        assistant_response = orchestrator.processChatMessage(query)
        for chunk in assistant_response.split():
            full_response += chunk + " "
            time.sleep(0.05)
            # Add a blinking cursor to simulate typing
            message_placeholder.markdown(full_response + "▌")
        message_placeholder.markdown(full_response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": full_response})
