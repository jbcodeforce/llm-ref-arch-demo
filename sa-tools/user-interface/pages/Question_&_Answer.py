import streamlit as st
import time
import os,sys
module_path = ".."
sys.path.append(os.path.abspath(module_path))
from orchestrator.Orchestrator import Orchestrator

orchestrator=Orchestrator()
st.set_page_config(page_title="Question", page_icon="./favicon.ico")

st.markdown("# Question to the knowledge base")
st.sidebar.header("Question & Answer")
st.write(
    """
    This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!
"""
)
# streamlit toggle
callWithVectorStore=st.toggle("Use your corpus", value=True,  help="Use the vector Store with RAG content",  label_visibility="visible")

response=""
with st.form('qa_form'):
    text = st.text_input("Ask a question","what is amazon bedrock?")
    submitted = st.form_submit_button('Submit')
    if submitted:
        with st.spinner("Processing..."):
            time.sleep(1)
        response= orchestrator.processHumanQuery(question=text,context="",useVectorStore=callWithVectorStore)
st.write(response)