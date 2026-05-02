from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_classic.chains.combine_documents import create_stuff_documents_chain  
from langchain_classic.chains.retrieval import create_retrieval_chain                           
from langchain_core.prompts import ChatPromptTemplate                         
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
import os

load_dotenv()
try:
    os.environ['HF_TOKEN'] = st.secrets["HF_TOKEN"]
    os.environ['GROQ_API_KEY'] = st.secrets["GROQ_API_KEY"]
except KeyError:
    # Fallback to .env file for local development
    os.environ['HF_TOKEN'] = os.getenv('HF_TOKEN', '')
    os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY', '')



def create_rag_chain():
    loader1 = PyPDFLoader("pdf's/Module 1_Introduction to Stock Markets.pdf")
    loader2 = PyPDFLoader("pdf's/Module 3_Fundamental Analysis.pdf")
    docs = loader1.load() + loader2.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    text = splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")  

    vector_store = FAISS.from_documents(text, embedding=embeddings)
    retriever = vector_store.as_retriever()

    prompt = ChatPromptTemplate.from_template("""
    You are a helpful financial advisor.
    Answer the question using the context below only.

    Context: {context}

    Question: {input}
    """)

    llm = ChatGroq(model="llama-3.1-8b-instant")  

    document_chain = create_stuff_documents_chain(llm=llm, prompt=prompt)
    rag_chain = create_retrieval_chain(retriever, document_chain)

    return rag_chain  

