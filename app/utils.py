import os
import csv
import requests
from bs4 import BeautifulSoup

def to_csv(data):
    csv_file = './data/drama_list.csv'
    
    fieldnames = [
        'title', 'native_title', 'rating', 'genres', 'directors', 
        'screenwriters', 'episodes', 'aired', 'aired_on', 'original_network', 
        'duration', 'content_rat', 'rank', 'popularity', 'watchers'
    ]
    
    if os.path.exists(csv_file):
        os.remove(csv_file)
        print(f"{csv_file} removed")
    
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for item in data:
            writer.writerow(item)
    print(f"{csv_file} written")

def fetch_main_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extract_drama_urls(soup):
    drama_urls = []
    for link in soup.select('a.block'):
        title = link.get_text(strip=True)
        url = 'https://mydramalist.com' + link['href']
        drama_urls.append({'title': title, 'url': url})
    return drama_urls
