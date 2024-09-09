from langchain.load import dumps, loads
from langchain_pinecone import PineconeVectorStore
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone
from dotenv import load_dotenv

from .multiple_query_generator import multiple_query_generation


import os

load_dotenv()

def get_unique_union(documents: list[list]):
    """ Unique union of retrieved docs """
    # Flatten list of lists, and convert each Document to string
    flattened_docs = [dumps(doc) for sublist in documents for doc in sublist]
    # Get unique documents
    unique_docs = list(set(flattened_docs))
    # Return
    return [loads(doc) for doc in unique_docs]


def retrieval_chain_init(selected_persona):
    pc = Pinecone(api_key=os.environ['PINECONE_API_KEY'])
    index = pc.Index('hackathon-awhom')
    embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
    
    vector_store = PineconeVectorStore(index=index, embedding=embeddings)
    
    retriever = vector_store.as_retriever(
        search_type="mmr",
        search_kwargs={"k": 5, "fetch_k": 10}
    )
    temp = multiple_query_generation(selected_persona=selected_persona)
    return temp | retriever.map() | get_unique_union