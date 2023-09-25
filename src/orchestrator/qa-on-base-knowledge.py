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


if __name__ == "__main__":
    aws_bedrock_client = bedrock.get_bedrock_client()
    embeddings=BedrockEmbeddings(client=aws_bedrock_client)
    chromaClient = Chroma(persist_directory="../embeddings",embedding_function=embeddings)

    query="what is the aws iam security policy?"
    print("--- Query: " + query)

    print("Use similarity search from vector store using embeddings")
    embedding_vector=   embeddings.embed_query(query)
    docs = chromaClient.similarity_search_by_vector(embedding_vector)
    print(docs[0].page_content)

    print(" Using Claude without any Retriever from vector store")
    llm= Bedrock(
                    client=aws_bedrock_client,
                    model_id="anthropic.claude-v1"
                ) 
    promptTemplare='''You are an expert in AWS service, so try to answer the following question:\n
    {question}\n'''
    llm_chain = LLMChain(llm=llm,
            prompt=PromptTemplate.from_template(promptTemplare)
    )
    result = llm_chain({"question": query})
    print_ww(result)

    print("Now use the vector store retriever")
   

    
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, return_source_documents=True)
    qa = ConversationalRetrievalChain.from_llm(llm, chromaClient.as_retriever(), memory=memory)
  
    docs = chromaClient.similarity_search(query)
    print(docs[0].page_content)
    result = qa({"question": query})
    print_ww(result["answer"])
    #print_ww(result["source_documents"][0])
    
    # print_ww(result["source_documents"])
    # print_ww(result["source_documents"])
    