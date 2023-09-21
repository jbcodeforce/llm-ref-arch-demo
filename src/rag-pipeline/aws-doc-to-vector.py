'''
This module is used to populate vectors from a set of AWS product documentation pages.
'''
from langchain.document_loaders import AsyncChromiumLoader
from langchain.document_transformers import BeautifulSoupTransformer

urlsToParse = []