import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse




def crawl_website(base_url, max_pages=5):
  visited = set()
  to_visit = [base_url]
  pages = []


  while to_visit and len(visited) < max_pages:
   url = to_visit.pop(0)
   if url in visited:
    continue


  response = requests.get(url)
  soup = BeautifulSoup(response.text, "html.parser")
  title = soup.title.string if soup.title else ""


  pages.append({
  "url": url,
  "title": title,
  "html": response.text
   })


  visited.add(url)


  for link in soup.find_all("a", href=True):
   full_url = urljoin(base_url, link['href'])
   if urlparse(full_url).netloc == urlparse(base_url).netloc:
    if full_url not in visited:
     to_visit.append(full_url)

  return pages