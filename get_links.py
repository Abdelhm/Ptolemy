"""
 get content and hyperlins from a wikipedia page
"""

# import package
import requests
s = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "parse",
    "page": "Pet door",
    "format": "json"
}

r = s.get(url=URL, params=PARAMS)
data = r.json()

print(data["parse"]["text"]["*"])
