from crawler import crawl_website
from extractor import extract_text
from chunker import chunk_pages
from embeddings import create_embeddings
from vector_store import build_vector_store
from retriever import retrieve_context


from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama


# Crawl & prepare data
pages = crawl_website("https://example.com")
cleaned_pages = extract_text(pages)
chunks = chunk_pages(cleaned_pages)


# Vector DB
embeddings = create_embeddings()
vector_store = build_vector_store(chunks, embeddings)


# Prompt
rag_prompt = ChatPromptTemplate.from_messages([
("system",
"You are a Q&A support assistant using Retrieval Augmented Generation (RAG). "
"Answer ONLY from the provided context. "
"If the answer is not present, say: "
"'I’m sorry, I couldn’t find the answer in the available information.'"),
("human", "Context:\n{context}\n\nQuestion:\n{question}")
])


llm = ChatOllama(model="llama3", temperature=0)




def answer_question(question):
 context = retrieve_context(vector_store, question)
 response = llm.invoke(rag_prompt.format(context=context, question=question))
 return response.content




print(answer_question("What is this website about?"))