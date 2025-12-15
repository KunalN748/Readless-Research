from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
import os
from django.conf import settings

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
