import os
from fastapi import FastAPI
from pydantic import BaseModel
from app.rag_pipeline import RAGPipeline
from app.memory import get_memory
from app.utils import format_retrieved_docs
from langchain_community.llms import HuggingFaceHub
from langchain.chains import ConversationalRetrievalChain

# Initialize FastAPI app
app = FastAPI()

# Initialize RAG pipeline
rag_pipeline = RAGPipeline()
documents = rag_pipeline.parse_documents("documents")
rag_pipeline.chunk_and_embed(documents)
rag_pipeline.save_vector_store("vector_store")

# Load Vector Store
rag_pipeline.load_vector_store("vector_store")

# Initialize conversational memory
memory = get_memory()

# Initialize dummy LLM for now (or ChatOpenAI if you have API key)
# You can also swap this with HuggingFace local LLM if you want free solution
from langchain_community.llms import HuggingFacePipeline
from transformers import pipeline
# Load local pipeline
local_pipeline = pipeline("text2text-generation", model="google/flan-t5-small")

llm = HuggingFacePipeline(pipeline=local_pipeline)


# Build Conversational Retrieval Chain
qa_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=rag_pipeline.vector_store.as_retriever(),
    memory=memory
)

# Request schema
class QueryRequest(BaseModel):
    query: str

# POST endpoint
@app.post("/chat")
async def chat_endpoint(request: QueryRequest):
    query = request.query
    result = qa_chain.invoke({"question": query})

    retrieved_docs = rag_pipeline.retrieve_relevant_docs(query)
    formatted_refs = format_retrieved_docs(retrieved_docs)

    return {
        "answer": result["answer"],
        "references": formatted_refs
    }
