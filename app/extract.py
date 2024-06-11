import requests
from bs4 import BeautifulSoup

def fetch_drama_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extract_drama_details(soup):
    title = ""
    rating = ""
    genres = ""
    native_title = ""
    directors = ""
    screenwriters = ""
    episodes = ""
    aired = ""
    aired_on = ""
    original_net = ""
    duration = ""
    content_rat = ""
    rank = ""
    populartiy = ""
    watchers = ""
    
    try:
        title = soup.find('h1').get_text(strip=True)
        hfs_class = soup.select_one('.hfs')
        rating = hfs_class.find('b').get_text(strip=True)
        
        genres_element = soup.find('li', class_='list-item p-a-0 show-genres')
        genres = genres_element.find_all('a')
        genres = [genre.get_text(strip=True) for genre in genres]
        
        details = soup.find_all('li', class_='list-item p-a-0')
        for detail in details:
            detail_text = detail.get_text(strip=True)
    
            if "Native Title:" in detail_text:
                try:
                    native_title = detail.find('a').get_text(strip=True)
                except:
                    pass
                
            if "Director:" in detail_text:
                try:
                    directors = [a.get_text(strip=True) for a in detail.find_all('a')]
                except:
                    pass
                
            if "Screenwriter:" in detail_text:
                try:
                    screenwriters = [a.get_text(strip=True) for a in detail.find_all('a')]
                except:
                    pass
                
            if "Episodes:" in detail_text:
                try:
                    episodes = detail_text.split(":")[1].strip()
                except:
                    pass
                
            if "Aired:" in detail_text:
                try:
                    aired = detail_text.split(":")[1].strip()
                except:
                    pass
                
            if "Aired On:" in detail_text:
                try:
                    aired_on = detail_text.split(":")[1].strip()
                except:
                    pass
                
            if "Original Network:" in detail_text:
                try:
                    original_net = [a.get_text(strip=True) for a in detail.find_all('a')]
                except:
                    pass
                
            if "Duration:" in detail_text:
                try:
                    duration = detail_text.split(":")[1].strip()
                except:
                    pass
                
            if "Content Rating:" in detail_text:
                try:
                    content_rat = detail_text.split(":")[1].strip()
                except:
                    pass
                
            if "Ranked:" in detail_text:
                try:
                    rank = detail_text.split(":")[1].strip()
                except:
                    pass
                
            if "Popularity:" in detail_text:
                try:
                    populartiy = detail_text.split(":")[1].strip()
                except:
                    pass
                
            if "Watchers:" in detail_text:
                try:
                    watchers = detail_text.split(":")[1].strip()
                except:
                    pass
        
        return {
            'title': title, 
            'native_title': native_title,
            'rating': rating, 
            'genres': genres, 
            'directors': directors,
            'screenwriters': screenwriters,
            'episodes': episodes,
            'aired': aired,
            'aired_on': aired_on,
            'original_network': original_net,
            'duration': duration,
            'content_rat': content_rat,
            'rank': rank,
            'popularity': populartiy,
            'watchers': watchers
        }
    
    except Exception as e:
        print(e)
