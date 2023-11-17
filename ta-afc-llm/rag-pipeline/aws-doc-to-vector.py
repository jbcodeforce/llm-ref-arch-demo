'''
This module is used to populate vectors from a set of cloud provider's product documentation pages.
'''
from langchain.document_loaders import AsyncHtmlLoader
from langchain.document_transformers import BeautifulSoupTransformer
from langchain.vectorstores import Chroma
from langchain.embeddings import BedrockEmbeddings
from langchain.document_loaders import UnstructuredMarkdownLoader

from langchain.text_splitter import TokenTextSplitter, MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

from langchain.document_loaders import DirectoryLoader

import os,sys
module_path = ".."
sys.path.append(os.path.abspath(module_path))
from utils import bedrock, print_ww


def loadDocumentsFromURLs(urlsToParse):
    print("--- Load documents from " + urlsToParse[0])
    loader = AsyncHtmlLoader(urlsToParse)
    html = loader.load()
    transformer = BeautifulSoupTransformer()
    docs_transformed = transformer.transform_documents(html,tags_to_extract=["h2","h3","h4","h5","h6","p","li","ul","ol","blockquote","pre","code","img","strong","em","a","table","tr","td","th"])
    # print_ww(docs_transformed[0].page_content[0:500])
    return docs_transformed

def splitInChunks(documents):
    print("--- Split in chunks ")
    text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 1000,
    chunk_overlap  = 0,
    )
    return text_splitter.split_documents(documents)

def createEmbeddings():
    aws_bedrock_client = bedrock.get_bedrock_client()
    #llm = Bedrock(model_id="anthropic.claude-v1", client=aws_bedrock_client, model_kwargs={'max_tokens_to_sample':200})
    return BedrockEmbeddings(client=aws_bedrock_client)

if __name__ == "__main__":
    urlsToParse = ["https://docs.aws.amazon.com/awssupport/latest/user/get-started-with-aws-trusted-advisor.html",
                   "https://docs.aws.amazon.com/awssupport/latest/user/cost-optimization-checks.html"]
    docs=loadDocumentsFromURLs(urlsToParse)
    chunks=splitInChunks(docs)
    embeddings=createEmbeddings()
    chromaClient = Chroma(persist_directory="../embeddings",embedding_function=embeddings)
    chromaClient.add_documents(chunks[0])
    print(chromaClient._collection.count())

    
    

    