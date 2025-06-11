# RAG Assignment Solution - Aelum Consulting

## Project Summary

This is a RAG-based chatbot system that can answer questions from a set of provided documents (PDFs).  
It uses a Vector Store + LLM (GPT-3.5) with conversational memory.

### Features

✅ Document parsing and chunking  
✅ Embeddings stored in FAISS  
✅ Conversational Memory  
✅ API endpoint (`/chat`)  
✅ References with page numbers  
✅ Unit tests  
✅ Async API  
✅ Containerized with Docker

---

## How to Run Locally

### 1️⃣ Clone repo and unzip documents

```bash
git clone https://github.com/your/repo.git
cd repo
unzip "RAG assignment documents.zip" -d documents
