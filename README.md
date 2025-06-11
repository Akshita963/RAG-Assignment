# 📚 Retrieval-Augmented Generation (RAG) Chatbot — Assignment

A document-aware chatbot built using **LangChain**, **HuggingFace**, **FAISS**, and **FastAPI**.

This project demonstrates **Retrieval-Augmented Generation (RAG)** — where a language model generates answers grounded in your own documents (e.g., PDFs).

---

## 🔍 What is RAG?

Traditional LLMs like ChatGPT can't access custom documents.  
**RAG solves this** by:

- Reading and chunking your PDFs
- Embedding and indexing them in a vector database
- Searching for relevant parts at query time
- Generating answers based on retrieved content

---

## ✅ Features Implemented

| Feature                        | Description                                |
|-------------------------------|--------------------------------------------|
| 📄 Document Parsing           | ✅ via PyMuPDF                              |
| ✂️ Chunking                   | ✅ using LangChain TextSplitter             |
| 🧠 Embeddings                 | ✅ HuggingFace `all-MiniLM-L6-v2`           |
| 📦 Vector Store               | ✅ FAISS                                    |
| 🤖 Question Answering         | ✅ FLAN-T5-small via HuggingFace            |
| 💬 Conversational Memory      | ✅ LangChain BufferMemory                   |
| 🧾 Metadata (page, file)      | ✅ included in responses                    |
| 🌐 REST API                   | ✅ FastAPI `/chat` endpoint                 |
| 🧪 Unit Tests                 | ✅ via Pytest                               |
| 🐳 Dockerfile                 | ✅ included (not executed locally)          |

---

## 🛠️ How to Run Locally

### 1. Clone the repo & install dependencies

```bash
git clone https://github.com/Akshita963/RAG-Assignment.git
cd RAG-Assignment
python -m venv venv
venv\Scripts\activate   # Or `source venv/bin/activate` on Linux/Mac
pip install -r requirements.txt

### 2. Place documents

```bash
Place your PDFs inside the documents/ folder.

### 3. Run the FastAPI server

```bash
uvicorn app.main:app --reload




