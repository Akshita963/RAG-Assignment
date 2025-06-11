import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyMuPDFLoader

class RAGPipeline:
    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        self.vector_store = None

    def parse_documents(self, doc_folder):
        print("Parsing documents...")
        docs = []
        for filename in os.listdir(doc_folder):
            if filename.endswith(".pdf"):
                loader = PyMuPDFLoader(os.path.join(doc_folder, filename))
                documents = loader.load()
                for doc in documents:
                    doc.metadata["source_file"] = filename
                docs.extend(documents)
        return docs

    def chunk_and_embed(self, documents):
        print("Chunking and embedding...")
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )
        chunks = splitter.split_documents(documents)
        self.vector_store = FAISS.from_documents(chunks, self.embedding_model)
        print("Embedding done!")

    def save_vector_store(self, path):
        if self.vector_store:
            self.vector_store.save_local(path)

    def load_vector_store(self, path):
        self.vector_store = FAISS.load_local(path, self.embedding_model,allow_dangerous_deserialization=True)

    def retrieve_relevant_docs(self, query, k=5):
        if not self.vector_store:
            raise Exception("Vector store not initialized!")
        return self.vector_store.similarity_search(query, k=k)
