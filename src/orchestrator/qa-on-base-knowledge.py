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

    
    #memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, return_source_documents=True)
    #qa = ConversationalRetrievalChain.from_llm(llm, chromaClient.as_retriever(), memory=memory)
  
    #docs = chromaClient.similarity_search(query)
    #print(docs[0].page_content)
    #result = qa({"question": query})
    #print_ww(result["answer"])
    #print_ww(result["source_documents"][0])
    
    # print_ww(result["source_documents"])
    # print_ww(result["source_documents"])
    