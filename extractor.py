from bs4 import BeautifulSoup




def extract_text(pages):
  cleaned_pages = []


  for page in pages:
   soup = BeautifulSoup(page['html'], "html.parser")
  for tag in soup(["script", "style", "nav", "footer"]):
   tag.decompose()


  text = soup.get_text(separator=" ", strip=True)


  cleaned_pages.append({
  "url": page['url'],
  "title": page['title'],
  "text": text
  })


  return cleaned_pages