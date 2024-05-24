import pandas as pandas
import numpy as np
from bs4 import BeautifulSoup
import requests
import time
import random


def imdbId_to_url(imdbId):
    return "https://www.imdb.com/title/tt0" + imdbId + "/"

def open_page(url: str,
                      sleep: bool = True,
                      headers: dict = {
                                      'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36",
                                      }) -> BeautifulSoup:
    if not url.startswith("https://www.imdb.com/title/tt"):
        raise ValueError("Invalid URL")
    
    response = requests.request("GET", url, headers=headers, verify=False)
    soup = BeautifulSoup(response.content)
    
    if sleep:
        time.sleep(random.randint(1, 5))
    
    return soup

def get_review_url(imdbId :str)->str:
    return "https://www.imdb.com/title/tt0"+imdbId+"/reviews?sort=totalVotes&dir=desc&ratingFilter=0"

# def get_review_url(soup: BeautifulSoup) -> str:
#     section = soup.find('section', {'data-testid': 'UserReviews'})
#     if section:
#         a_tag = section.find('a')
        
#         if a_tag:
#             return "https://www.imdb.com" + a_tag['href']
#         else:
#             return "Hyperlink not found within the specified section."
#     else:
#         return "Section with the specified data-testid not found."