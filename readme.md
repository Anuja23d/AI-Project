# RAG Q&A Support Bot (Gemini)

This project implements a Question & Answer support bot using
Retrieval Augmented Generation (RAG).

## Features
- Website crawling
- Text cleaning & chunking
- Vector embeddings using Gemini
- FAISS vector database
- Context-aware answers
- Hallucination-safe responses

## Tech Stack
- Python
- LangChain
- Google Gemini
- FAISS
- BeautifulSoup

## How It Works
1. Crawl website content
2. Chunk and embed text
3. Store embeddings in FAISS
4. Retrieve relevant chunks
5. Generate answers using Gemini

## Rule
The bot answers strictly from retrieved content.
If no answer is found, it responds accordingly.
