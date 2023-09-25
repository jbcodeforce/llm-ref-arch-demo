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


def loadMarkdownDocs(markdown_path):
    '''
    Load all md file from the given directory. Flat at this stage.
    return a list of documents like the following
    Document(page_content='Networking', metadata={'source': 'docs/networking.md', 'filename':
'networking.md', 'file_directory': 'docs', 'last_modified': '2023-09-23T18:33:24', 'filetype':
'text/markdown', 'page_number': 1, 'category': 'Title'})
    '''
    elements = []
    for doc in os.listdir(markdown_path):
        fileName = markdown_path+doc
        print("--- Load markdown doc " + fileName)
        loader = UnstructuredMarkdownLoader(
                    fileName, mode="elements")
        elements.append(loader.load())
    return elements


def createEmbeddings():
    aws_bedrock_client = bedrock.get_bedrock_client()
    #llm = Bedrock(model_id="anthropic.claude-v1", client=aws_bedrock_client, model_kwargs={'max_tokens_to_sample':200})
    return BedrockEmbeddings(client=aws_bedrock_client)


if __name__ == "__main__":
    chunks=loadMarkdownDocs("docs/")
    embeddings=createEmbeddings()
    chromaClient = Chroma(persist_directory="../embeddings",embedding_function=embeddings)
    chromaClient.add_documents(chunks[0])
    
    print(chromaClient._collection.count())
    
    

    