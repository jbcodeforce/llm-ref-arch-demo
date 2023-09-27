
from langchain.vectorstores import Chroma
from langchain.embeddings.sentence_transformer import SentenceTransformerEmbeddings
from sentence_transformers import util

query = "load balancers configured with a missing security group"
embeddings=SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
chromaClient = Chroma(persist_directory="../embeddings",embedding_function=embeddings)
   
docs = chromaClient.similarity_search_with_relevance_scores(query)
print(docs)
queryVector = embeddings.embed_query(query)
for doc, score in docs:
    #docVector = embeddings.embed_query(doc.page_content)
    #cosine_scores = util.cos_sim(queryVector, docVector)
    #print("{} \t\t {} \t\t Score: {:.4f}".format(query, doc.page_content, cosine_scores[0][0]))
    print("{} \t\t {} \t\t Score: {:.4f}".format(query, doc.page_content, score))