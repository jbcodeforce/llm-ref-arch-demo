'''
Orchestrator leveraging existing VectorStore, define a prompt to get some question
answered from a LLM
'''
from langchain.embeddings import BedrockEmbeddings
from langchain.llms.bedrock import Bedrock
from langchain.chains import RetrievalQA,RetrievalQAWithSourcesChain,LLMChain
from langchain.prompts import PromptTemplate
from langchain.vectorstores import OpenSearchVectorSearch

import os,sys
module_path = ".."
sys.path.append(os.path.abspath(module_path))
from utils import bedrock



class Orchestrator:
    
    def __init__(self):
        self.aws_bedrock_client = bedrock.get_bedrock_client()
        OPENSEARCH_HOST=os.environ.get("OPENSEARCH_HOST","https://localhost:9200")
        OPENSEARCH_PWD=os.environ.get("OPENSEARCH_PWD","admin")
        OPENSEARCH_INDEX=os.environ.get("OPENSEARCH_INDEX","aws_bedrock_corpus")
        embeddings=BedrockEmbeddings(model_id="amazon.titan-embed-text-v1",client=self.aws_bedrock_client)
        self.docsearch=OpenSearchVectorSearch(
                index_name=OPENSEARCH_INDEX,
                embedding_function=embeddings,
                opensearch_url=OPENSEARCH_HOST,
                http_auth=("admin", OPENSEARCH_PWD),
                use_ssl = False,
                verify_certs = False,
                ssl_assert_hostname = False,
                ssl_show_warn = False
        )
        print(OPENSEARCH_HOST)
        
        
    
    def definePrompt(self):
        promptTemplate='''
Human: Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Use three sentences maximum and keep the answer as concise as possible. 
Always say "thanks for asking!" at the end of the answer.
\n
        {context}
\n
{question} \n
\n
Assistant: 
'''
        return PromptTemplate(template=promptTemplate, input_variables=["context", "question"])

    def processHumanQuery(self,question: str, context: str, useVectorStore= True, temperature=0.5, top_p=0.9):
        inference_modifier = {'max_tokens_to_sample':4096, 
                      "temperature": temperature,
                      "top_k":250,
                      "top_p": top_p,
                      "stop_sequences": ["\n\nHuman"]
                     }
        llm= Bedrock(
                        client=self.aws_bedrock_client,
                        model_id="anthropic.claude-v2",
                        model_kwargs = inference_modifier 
                )
        print("--- Query: " + question)
        prompt=self.definePrompt() 
        print(prompt.format(context=context, question=question))
        if useVectorStore:
            qa_chain = RetrievalQA.from_chain_type(
                    llm=llm,
                    chain_type="stuff",
                    retriever=self.docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3}),
                    chain_type_kwargs={"prompt": prompt   }
                    )
            result = qa_chain({"query":question})
            return result["result"]
        else:
            qa_chain = LLMChain(llm=llm, prompt=prompt)
            result=qa_chain.run({"question":question, "context":context})
            print(result)
            return result



    def processChatMessage(self,humanMessage):
        return "Got it"