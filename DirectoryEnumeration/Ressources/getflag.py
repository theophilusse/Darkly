#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup

BASE_URL = "http://192.168.56.101/.hidden"

def scrape_recursive(url, session, depth=0):
    r = session.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    
    # Cherche le flag dans le contenu
    text = soup.get_text()
    #if "README" in url:
        #print(text)
    if "flag" in text.lower() or "FLAG" in text:
        print(f"[+] FLAG TROUVE à {url}")
        print(text[:500])
    
    # Récupère tous les liens enfants
    for link in soup.find_all("a", href=True):
        href = link["href"]
        if href not in ("../", "/") and not href.startswith("http"):
            #print(f"{url}/{href.rstrip('/')}")
            scrape_recursive(f"{url}/{href.rstrip('/')}", session, depth+1)

session = requests.Session()
scrape_recursive(BASE_URL, session)
