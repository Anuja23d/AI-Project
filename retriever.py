

def retrieve_context(vector_store, query, k=3):
 docs = vector_store.similarity_search(query, k=k)
 return "\n\n".join(doc.page_content for doc in docs)