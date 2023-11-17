'''
Orchestrator leveraging existing VectorStore, define a prompt to get some question
answered from a LLM
'''
from langchain.vectorstores import Chroma
from langchain.embeddings import BedrockEmbeddings
from langchain.llms.bedrock import Bedrock
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate, StringPromptTemplate
from langchain.chains import ConversationalRetrievalChain, LLMChain
from langchain.memory import ConversationBufferMemory

import os,sys
module_path = ".."
sys.path.append(os.path.abspath(module_path))
from utils import bedrock, print_ww

class Orchestrator:
    
    def __init__(self):
        self.aws_bedrock_client = bedrock.get_bedrock_client()
        embeddings=BedrockEmbeddings(client=self.aws_bedrock_client)
        self.chromaClient = Chroma(persist_directory="../embeddings",embedding_function=embeddings)
        
    
    def definePrompt(self):
        promptTemplate='''
        Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Use three sentences maximum and keep the answer as concise as possible. 
Always say "thanks for asking!" at the end of the answer. 
{context}
Question: {question}
Helpful Answer:'''
        return PromptTemplate(template=promptTemplate, input_variables=["context", "question"])

    def processHumanQuery(self,question, temperature=0.1, top_p=0.9):
        llm= Bedrock(
                        client=self.aws_bedrock_client,
                        model_id="anthropic.claude-v1"
                )
        print("--- Query: " + question)
        qa_chain = RetrievalQA.from_chain_type(
                    llm=llm,
                    chain_type="stuff",
                    retriever=self.chromaClient.as_retriever(search_type="similarity", search_kwargs={"k": 3}),
                    chain_type_kwargs={"prompt": self.definePrompt()    }
                    )
        result = qa_chain({"query": question})
        return result["result"]


