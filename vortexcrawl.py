import requests
from bs4 import BeautifulSoup
import sys
import os

def banner():
    os.system('clear')
    print("\033[1;34m") # Blue
    print("      [ VORTEX - Web Spider & Crawler ]")
    print("\033[0m")

def crawl():
    banner()
    url = input("\n\033[1;36m[?] Enter Target URL (http://...): \033[0m")
    
    try:
        print(f"\n\033[1;33m[*] Crawling {url}...\033[0m")
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        
        links = soup.find_all('a')
        print(f"\033[1;32m[+] Found {len(links)} links:\033[0m\n")
        
        for link in links:
            href = link.get('href')
            if href and href.startswith('http'):
                print(f"  > {href}")
                
    except Exception as e:
        print(f"\033[1;31m[!] Error: {e}\033[0m")

if __name__ == "__main__":
    crawl()

