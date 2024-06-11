import time
from utils import fetch_main_page, extract_drama_urls, to_csv
from extract import fetch_drama_page, extract_drama_details

def main():
    drama_details = []
    
    for i in range(1, 58):
        try:
            main_url = f'https://mydramalist.com/search?adv=titles&ty=68,83&co=3&re=2020,2024&rt=4,10&st=3&so=top&page={i}'
            
            main_soup = fetch_main_page(main_url)
            drama_urls = extract_drama_urls(main_soup)
            
            for drama in drama_urls:
                drama_soup = fetch_drama_page(drama['url'])
                details = extract_drama_details(drama_soup)
                drama_details.append(details)
                
                print(drama_details)
                
                time.sleep(1)
            
            print(f"-------------------------Page-{i}-------------------------")
        except Exception as e:
            print(e)
    
    try:
        to_csv(drama_details)
    except Exception as e:
        print(e)
        
if __name__ == "__main__":
    main()
