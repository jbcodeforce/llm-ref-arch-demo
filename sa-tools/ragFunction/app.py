import os, json
import sys, boto3
from timeit import default_timer as timer
'''
Function to add a specified file to the OpenSearch vector store
'''
module_path = ".."
sys.path.append(os.path.abspath(module_path))
from utils import bedrock
from langchain.embeddings import BedrockEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.vectorstores import OpenSearchVectorSearch

OPENSEARCH_HOST=os.environ.get("OPENSEARCH_HOST","https://localhost:9200")
OPENSEARCH_PWD=os.environ.get("OPENSEARCH_PWD","admin")
OPENSEARCH_INDEX=os.environ.get("OPENSEARCH_INDEX","aws_bedrock_corpus")
# Code will be create before lambda callback
aoss_client = boto3.client('opensearchserverless')
bedrock_runtime = bedrock.get_bedrock_client(
    assumed_role=os.environ.get("BEDROCK_ASSUME_ROLE", None),
    region=os.environ.get("AWS_DEFAULT_REGION", None),
)
embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v1", client=bedrock_runtime)

# add a lambda handler function
def lambda_handler(event, context):
    # get the S3 object path from the event
    file_path = event['s3_object_path']
    # add the file to the vector store
    response_body=add_file_to_vector_store(file_path,OPENSEARCH_INDEX)
    # return the file path
    return {
        'statusCode': 200,
        'body': json.dumps({
            'generated-text': response_body
        })
    }


def add_file_to_vector_store(s3_object_path, corpus_name):

    start = timer()         
    print("Load source PDF documents from bucket or folder")
    loader = PyPDFDirectoryLoader(s3_object_path)
    end = timer() 
    print("--> Load document from source took %d s" % (end - start))
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "], #split chunks at (1) paragraph, (2) line, (3) sentence, or (4) word, in that order
        chunk_size = 1000,
        chunk_overlap  = 100,
    )
    print("Build chunks")
    docs = text_splitter.split_documents(documents)
    print("--> Number of chunks %d" % len(docs))
    print("Upload to opensearch " + OPENSEARCH_HOST + " using embeddings")
    start = timer()
    docsearch = OpenSearchVectorSearch.from_documents(
        docs, 
        embeddings, 
        bulk_size=1100,
        index_name=corpus_name,
        opensearch_url=OPENSEARCH_HOST,
        http_auth=("admin", OPENSEARCH_PWD),
        use_ssl = False,
        verify_certs = False,
        ssl_assert_hostname = False,
        ssl_show_warn = False,)
    end = timer() 
    print("--> Embedding and saving to vector storetook %d2" % (end - start))
    return {"document chunks" : len(docs)}






# define main function
if __name__ == '__main__':
    rep=add_file_to_vector_store("./data",OPENSEARCH_INDEX)
    print(rep)
    print("Connect to opensearch to do a search")
    docsearch=OpenSearchVectorSearch(
        index_name=OPENSEARCH_INDEX,
        embedding_function=embeddings,
        opensearch_url=OPENSEARCH_HOST,
        http_auth=("admin", OPENSEARCH_PWD),
        use_ssl = False,
        verify_certs = False,
        ssl_assert_hostname = False,
        ssl_show_warn = False
        )

    # you can specify custom field names to match the fields you're using to store your embedding, document text value, and metadata
    docs = docsearch.similarity_search(
        "What is bedrock?",
        k=10
    )
    print(docs)
    print(docs[0].page_content)



