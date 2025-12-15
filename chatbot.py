from langchain_core.prompts import ChatPromptTemplate
import requests
from bs4 import BeautifulSoup
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama import ChatOllama
rag_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a Q&A support assistant using Retrieval Augmented Generation (RAG). "
     "Answer ONLY from the provided context. "
     "If the answer is not present, say: "
     "'I’m sorry, I couldn’t find the answer in the available information.'"
    ),
    ("human", 
     "Context:\n{context}\n\n"
     "Question:\n{question}"
    )
])
def crawl_website(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup.get_text(separator=" ", strip=True)

text = crawl_website("https://example.com")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = splitter.split_text(text)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vector_store = FAISS.from_texts(chunks, embeddings)
def retrieve_context(question, k=3):
    docs = vector_store.similarity_search(question, k=k)
    return "\n\n".join([doc.page_content for doc in docs])

llm = ChatOllama(
    model="llama3",
    temperature=0
)

def answer_question(question):
    context = retrieve_context(question)
    response = llm.invoke(
        rag_prompt.format(
            context=context,
            question=question
        )
    )
    return response.text

print(answer_question("What is this website about?"))