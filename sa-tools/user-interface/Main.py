import streamlit as st
from st_pages import Page, show_pages, add_page_title

from PIL import Image

im = Image.open("favicon.ico")
st.set_page_config(
    page_title="Introduction",
    page_icon=im,
)


st.write("# Welcome to AnyCompany for Consultants")

tab1, tab2, tab3 = st.tabs(["Home", "Context", "Deployment"])

with tab1:
    

    st.markdown(
        """
    This demonstration illustrates integration with AWS Bedrock with one of the LLM. 
    The user interface application is done with Streamlit, an open source app framework built specifically for Machine Learning and Data Science projects

**👈 Select a demo from the left sidebar**!

### Want to learn more?

- Amazon [Bedrock](https://aws.amazon.com/bedrock)
- User interface is done with [streamlit.io](https://docs.streamlit.io)
- The [Git Repository](https://github.com/jbcodeforce/llm-ref-arch-demo) for this demo.
        
"""
)

with tab2:
    st.write("# Context")
    st.write(
        """
    The example is about an ISV with a team of professional service developing deisgn documents, architecture decision documents,
    code, scripts to help deploying the ISV software product on-premises or on a cloud provider. This corpus of knowledge
    is poorly managed, and not semantic search exists, or summarization capability. The goal is to build a solution
    to help new consultant to learn, get answer to questions and generate text to better answer customer's questions.  
    """
    )
    st.image("images/llm-discovery.png")

with tab3:
    st.write("# Deployment")
    st.write("The solution includes at least two paths: the documents ingestion and the application to interact with the consultants.")

    st.markdown("""
## Ingestion deployment architecture

The consultant  can  upload  the  design  documents,  architecture  decision  documents,  code,  scripts  to the data lake. The document could be 
processed as-is, but it may be recommended to do some simple document pruning, to extract the meaningful part of the documentation, and reduce the size
of the document to process. The document is splitted in chunks, which are then encoded in a vector format using Amazon Titan Embedding deployed in Bedrock Service.
The resulting vectors are saved in OpenSearch used as Vector Store. Vector store has similarity function to help performing semantic search.
""")
    
    st.image("images/ingestion-deployment.png")

    st.markdown("""
## Application deployment architecture
The user interface is connected to an orchestrator to support the different use cases of the end user: Question and answer, chatbot.... The application
may be deployed as ECS task in a ECS cluster, and access Bedrock from a private subnet via Interface Endpoint of PrivateLink. Embedding and FM models are used
as well as the Vector Store to build a RAG context.
""")
                
    st.image("images/deployment.png")

with st.sidebar:
    
    show_pages(
    [
        Page("Main.py", "Home", "🏠"),
        Page("pages/Question_&_Answer.py", "Question & Answer",":question:"),
        Page("pages/Chat_Bot.py", "Chat Bot", "💬"),
        Page("pages/Price_calculator.py", "Price Calculator", "$"),
        Page("pages/Manage_Asset.py", "Manage Assets", ":book:"),
    ]
)