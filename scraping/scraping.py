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

def get_reviews(imdb_id: str):
    url = get_review_url(imdb_id)
    soup = open_page(url)
    reviews = []
    for review in soup.find_all("div", class_="lister-item-content"):
        reviews.append(review.find("div", class_="text show-more__control").text)
    review_dict = {}
    review_dict[imdb_id] = reviews
    return review_dict