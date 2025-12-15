from langchain_community.vectorstores import FAISS




def build_vector_store(chunks, embeddings):
 texts = [chunk['text'] for chunk in chunks]
 metadatas = [{"url": c['url'], "title": c['title']} for c in chunks]
 return FAISS.from_texts(texts, embeddings, metadatas=metadatas)