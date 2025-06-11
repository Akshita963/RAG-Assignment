def format_retrieved_docs(docs):
    formatted = []
    for doc in docs:
        page_number = doc.metadata.get("page", "Unknown")
        source_file = doc.metadata.get("source_file", "Unknown")
        formatted.append(f"[{source_file}, Page {page_number}] {doc.page_content[:200]}...")
    return formatted
