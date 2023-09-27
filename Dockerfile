
FROM python:latest
ENV PATH=/root/.local/bin:$PATH

ENV PYTHONPATH=/app

RUN pip install --upgrade pip \
  && pip install wget requests  numpy pandas xlrd scikit-learn keras  bs4
USER $USER
EXPOSE 8501 5000 8888 7860
# install NLP packages: 
RUN pip install -U  nltk  gensim  
# install llm package
RUN pip install langchain openai boto3 gradio chromadb unstructured markdown tiktoken streamlit
WORKDIR /app