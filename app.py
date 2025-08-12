# app.py
import os
from langchain.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA

# Path to the FAISS database
DB_FAISS_PATH = 'faiss_db'

# Custom prompt template for the chatbot's QA system
custom_prompt_template = """You are a medical chatbot. Use the following pieces of information to answer the user's question.
If you don't know the answer, say that you don't know. Do not attempt to fabricate an answer.

Context: {context}
Question: {question}

Please provide a concise and factual response.
Helpful answer:
"""

def set_custom_prompt():
    """Return the custom prompt template."""
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=['context', 'question'])
    return prompt

def load_llm():
    """Load the Llama-2 model for answering questions."""
    llm = CTransformers(
        model="TheBloke/Llama-2-7B-Chat-GGML",
        model_type="llama",
        max_new_tokens=512,
        temperature=0.5
    )
    return llm

def retrieval_qa_chain(llm, prompt, db):
    """Retrieve relevant documents from FAISS and generate answers using the Llama-2 model."""
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",  # You can change this to "map_reduce" for larger documents
        retriever=db.as_retriever(search_kwargs={'k': 2}),  # Retrieve top 2 relevant docs
        return_source_documents=True,
        chain_type_kwargs={'prompt': prompt}
    )
    return qa_chain

def qa_bot():
    """Main function to set up the retrieval-augmented QA system."""
    # Load the FAISS database
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", model_kwargs={'device': 'cpu'})
    db = FAISS.load_local(DB_FAISS_PATH, embeddings, allow_dangerous_deserialization=True)
    
    # Load the Llama-2 model
    llm = load_llm()

    # Set up the custom prompt template
    qa_prompt = set_custom_prompt()

    # Create and return the retrieval-augmented QA chain
    qa_chain = retrieval_qa_chain(llm, qa_prompt, db)
    
    return qa_chain

def final_result(query):
    """Get the final result (answer) for a user query."""
    qa_result = qa_bot()
    response = qa_result({'query': query})
    return response
