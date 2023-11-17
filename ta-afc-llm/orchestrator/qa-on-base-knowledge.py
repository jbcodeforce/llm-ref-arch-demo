'''
Orchestrator leveraging existing VectorStore, define a prompt to get some question
answered from a LLM
'''
from langchain.vectorstores import Chroma
from langchain.embeddings import BedrockEmbeddings
from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate, StringPromptTemplate
from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain.memory import ConversationBufferMemory

import os,sys
module_path = ".."
sys.path.append(os.path.abspath(module_path))
from utils import bedrock, print_ww
from orchestrator.Orchestrator import Orchestrator


if __name__ == "__main__":
   

    query="load balancers configured with a missing security group?"
    orchestrator=Orchestrator()
    response= orchestrator.processHumanQuery(query)
    print_ww(response)