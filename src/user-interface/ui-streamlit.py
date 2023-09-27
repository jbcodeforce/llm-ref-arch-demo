import streamlit as st
#import replicate
import os,sys
module_path = ".."
sys.path.append(os.path.abspath(module_path))
from orchestrator.Orchestrator import Orchestrator

orchestrator_client = Orchestrator()

def generate_llm_response(query,temperature,top_p):
    return orchestrator_client.processHumanQuery(query,temperature,top_p)



st.set_page_config(
    page_title="Trusted Advisor Filtering Builder",
    page_icon=":robot:",
    layout="wide")

with st.sidebar:
  st.title('Trusted Advisor Filtering Builder')
  st.subheader('Parameters')
  temperature = st.sidebar.slider('temperature', min_value=0.01, max_value=5.0, value=0.1, step=0.01)
  top_p = st.sidebar.slider('top_p', min_value=0.01, max_value=1.0, value=0.9, step=0.01)
 
  st.markdown('📖 Learn about this app in this [repository](https://github.com/jbcodeforce/llm-ref-arch-demo)!')

if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "How may I assist you today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)


# User data
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Get the response

if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_llm_response(prompt,temperature,top_p)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)