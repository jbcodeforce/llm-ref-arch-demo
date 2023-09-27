'''
This module is used to populate vectors from a set of cloud provider's product documentation pages.
'''
from langchain.document_loaders import AsyncHtmlLoader
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from langchain.vectorstores import Chroma
from langchain.embeddings import BedrockEmbeddings
from langchain.document_loaders import UnstructuredMarkdownLoader
from langchain.document_loaders import DirectoryLoader

from langchain.text_splitter import TokenTextSplitter, MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter

from langchain.document_loaders import DirectoryLoader

import os,sys
module_path = ".."
sys.path.append(os.path.abspath(module_path))
from utils import bedrock, print_ww


def loadMarkdownDocsToChunks(markdown_path):
    '''
    Load all md files from the given directory. Flat at this stage.
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

'''
Load all md file from the given path, use text splitter
using headers to split the text.
The problem is that it return a big document, which is not nice.
'''
def loadMarkdownDocsToChunksWithHeader(markdown_path):
    headers_to_split_on = [("#", "Header 1"), ("##", "Header 2"), ("###", "Header 3")]
    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
    loader= DirectoryLoader(markdown_path, glob="**/*.md")    
    elements = []
    for document in loader.load():
        print(document)
        elements.append(markdown_splitter.split_text(document.page_content))
    return elements

def createBedrockEmbeddings():
    aws_bedrock_client = bedrock.get_bedrock_client()
    return BedrockEmbeddings(client=aws_bedrock_client)

if __name__ == "__main__":
    chunks=loadMarkdownDocsToChunks("docs/")
    #chunks=loadMarkdownDocsToChunksWithHeader("docs/")
    print(" --- chunks done !")
    # createBedrockEmbeddings()
    embeddings=SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
    chromaClient = Chroma(persist_directory="../embeddings",embedding_function=embeddings)
    print(" --- build vector store from chunks")
    chromaClient.add_documents(chunks[0])
    
    print(chromaClient._collection.count())
    # should more than 2500 docs.
    
    

    