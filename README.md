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

### 1. Clone the repo and install the dependencies

git clone https://github.com/Akshita963/RAG-Assignment.git
cd RAG-Assignment
python -m venv venv
venv\Scripts\activate   # Or `source venv/bin/activate` on Linux/Mac
pip install -r requirements.txt

### 2. Place documents

Place your PDFs inside the documents/ folder.

### 3. Run the FastAPI server

uvicorn app.main:app --reload


### 💬 Sample API Usage:

Endpoint: /chat (POST)

Request:
{
  "query": "what is SYNOPSIS OF THE STRANGE CASE OF DR. JEKYLL AND MR HYDE is about"
}

Response:
{
  "answer": "The Strange Case of Dr. Jekyll and Mr. Hyde is a short psychological horror novel, a true classic of universal literature that deals with a very human and complex theme.",
  "references": [
    "[6. Strange Case of Dr Jekyll and Mr Hyde, Robert Louis Stevenson.pdf, Page 0] THE STRANGE CASE \nOF DOCTOR JEKYLL \nAND MR. HYDE\nRobert Louis Stevenson\nInfoBooks.org...",
    "[6. Strange Case of Dr Jekyll and Mr Hyde, Robert Louis Stevenson.pdf, Page 1] SYNOPSIS OF THE STRANGE CASE OF DR. JEKYLL AND MR. \nHYDE \nThe Strange Case of Dr. Jekyll and Mr. Hyde is a short \npsychological horror novel, a true classic of universal literature \nthat deals with a ...",
    "[6. Strange Case of Dr Jekyll and Mr Hyde, Robert Louis Stevenson.pdf, Page 102] up and emptied by fever, languidly weak both in body and \nmind, and solely occupied by one thought: the horror of my \nother self. But when l slept, or when the virtue of the medicine \nwore off, l woul...",
    "[6. Strange Case of Dr Jekyll and Mr Hyde, Robert Louis Stevenson.pdf, Page 102] thought of Hyde, for all his energy of life, as of something not \nonly hellish but inorganic. This was the shocking thing; that the \nslime of the pit seemed to utter cries and voices; that the \namorph...",
    "[6. Strange Case of Dr Jekyll and Mr Hyde, Robert Louis Stevenson.pdf, Page 42] Hyde. Now that that evil influence had been withdrawn, a new \nlife began for Or. Jekyll. He came out of his seclusion, renewed \nrelations with his friends, became once more their familiar guest \nand e..."
  ]
}


### 🧠 How It Works:

PDFs are parsed and split into small text chunks
Each chunk is converted into a vector (embedding)
Vectors are stored in FAISS
User question is embedded and compared to the stored chunks
Top results are passed to the LLM to generate an answer
System returns answer + source page info

### 🔁 Conversational Memory:

The system remembers past questions within a session.
Example:
Ask: "Summarize the document."
Then: "Tell me more about that."
✅ Memory is managed by LangChain's ConversationBufferMemory.

### 🧪 Run Unit Tests and Docker Support(Bonus):

Unit test :
 $env:PYTHONPATH="."     # (Windows)
 pytest
 ✅ This checks PDF parsing, embedding, and retrieval pipeline.

🐳 Docker Support :
Although Docker wasn't run on my system due to local limitations,
a complete and working Dockerfile is included:

docker build -t rag-app .
docker run -p 8000:8000 rag-app
Then open: http://localhost:8000/docs

📂 Folder Structure:
├── app/                  # Main application code
├── documents/            # User documents (PDFs)
├── vector_store/         # FAISS DB storage
├── tests/                # Unit tests
├── Dockerfile            # Containerization support
├── .env.example          # Env file sample
├── requirements.txt      # Dependencies
└── README.md             # Project documentation

✅ Summary:
- FastAPI + LangChain-based RAG chatbot
- HuggingFace models — 100% FREE, no API keys required
- Memory support and document references
- Unit tests and Docker support included

