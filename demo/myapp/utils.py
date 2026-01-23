# learn Django: https://www.youtube.com/watch?v=2TJxpyO3ei4
# learn how to use AI on PDFs: https://www.youtube.com/watch?v=2TJxpyO3ei4

from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_community.embeddings.bedrock import BedrockEmbeddings


import os
from django.conf import settings

from get_embeddings_function import get_embeddings_function
from langchain_community.vectorstores import Chroma

# Define the path to your PDF data
DATA_PATH = os.path.join(settings.BASE_DIR, 'myapp', 'data')

def load_documents():
    """Load PDF documents from the data directory"""
    document_loader = PyPDFDirectoryLoader(DATA_PATH)
    return document_loader.load()

def split_documents(documents: list[Document]):
    """Split documents into smaller chunks for processing"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
    )  
    return text_splitter.split_documents(documents)

def add_to_chroma(chunks: list[Document]):
    db = Chroma(
        persist_directory= CHROMA_PATH, embedding_function=get_embeddings_function()
    )
    db.add_documents(new_chunks, ids = new_chunk_ids)
    db.persist()

    last_page_id = None
    current_chunk_index = 0

    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        current_page_id = f"{source}:{page}"

        #if the page ID is the same as the last one, increment the chunk index
        if current_page_id == last_page_id:
            current_chunk_index += 1
        else:
            current_chunk_index = 0
        
        #add it to the chunk meta-data
        chunk.metadata["id"] = chunk_id

        #add or update the docs
        existing_items = db.get(include=[]) #ids are always included by default
        existing_ids = set(existing_items['ids'])
        print(f"Number of existing documents in DB: {len(existing_ids)}")

        new_chunks = []
        for chunk in chunks_with_ids:
            if chunk.metadata["id"] not in existing_ids:
                new_chunks.append(chunk)
            new_chunks_ids = [chunk.metadata["id"] for chunk in new_chunks]
            db.add_documents(new_chunks, ids=new_chunk_ids) 
            db.persist()
    return db
CHROMA_PATH = os.path.join(settings.BASE_DIR, 'myapp', 'chroma_db')

def get_embeddings_function():
    embeddings = BedrockEmbeddings(
        credentials_profile_name='default', region_name='us-east-1'
    )
    return embeddings

def query_chroma(query: str, k: int = 5):
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embeddings_function()
    )
    results = db.similarity_search(query, k=k)
    return results