from app.rag_pipeline import RAGPipeline

def test_pipeline_loading():
    rag_pipeline = RAGPipeline()
    docs = rag_pipeline.parse_documents("documents")
    assert len(docs) > 0

    rag_pipeline.chunk_and_embed(docs)
    retrieved = rag_pipeline.retrieve_relevant_docs("What is this document about?")
    assert len(retrieved) > 0
