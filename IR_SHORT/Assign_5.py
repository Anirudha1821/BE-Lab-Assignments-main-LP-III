import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

def crawl(url, depth, visited=set()):
    if depth == 0 or url in visited:
        return
    print(f"Crawling: {url}")
    
    # Mark the current URL as visited
    visited.add(url)
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract all links
        for link in soup.find_all('a', href=True):
            href = link['href']
            full_url = urljoin(url, href)  # Convert relative URL to absolute URL
            
            # Check if the URL has already been visited
            if full_url not in visited:
                print(f"Found link: {full_url}")
                
                # Recursive call to crawl the found link with reduced depth
                crawl(full_url, depth - 1, visited)
                
    except requests.exceptions.RequestException as e:
        print(f"Failed to retrieve {url}: {e}")
    
    # Pause to prevent overloading the server
    time.sleep(1)

# Starting URL and depth
start_url = "http://example.com"
max_depth = 2

crawl(start_url, max_depth)
