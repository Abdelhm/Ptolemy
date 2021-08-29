"""
 get content and hyperlinks from a wikipedia page
"""

# import package
import requests
from bs4 import BeautifulSoup
import re
s = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "parse",
    "page": "Cat",
    "format": "json"
}

r = s.get(url=URL, params=PARAMS)
data = r.json()
content = data["parse"]["text"]["*"]

soup = BeautifulSoup(content)
links = soup.find_all('a', href=True)

links_infos = {}
wiki_links = []

for link in links:
    if re.match('/wiki/.*', link['href']):
        links_infos['link'] = link['href']
        links_infos['tag'] = link.text
        wiki_links.append(links_infos)
        links_infos = {}
    else:
        pass
