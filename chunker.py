from langchain_text_splitters import RecursiveCharacterTextSplitter




def chunk_pages(cleaned_pages):
 splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
 chunks = []


 for page in cleaned_pages:
  page_chunks = splitter.split_text(page['text'])
 for i, chunk in enumerate(page_chunks):
  chunks.append({
  "chunk_id": f"{page['url']}_{i}",
  "url": page['url'],
  "title": page['title'],
  "text": chunk
  })


 return chunks