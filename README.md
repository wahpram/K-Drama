# K-Drama Scraper

K-Drama Scraper is a Python script that scrapes Korean Drama 2020 - 2024 information from MyDramaList.com and saves it to a CSV file.

## Features

- Scrapes drama titles, ratings, genres, directors, screenwriters, episodes, airing information, and more.
- Saves scraped data to a CSV file for easy analysis and storage.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your_username/drama-scraper.git

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

## Usage

1. Run the 'main.py' script:

    ```bash
    python main.py

2. The script will scrape drama information from MyDramaList.com and save it to a CSV file located in the 'data' directory.

## File Structure

    /K-Drama-Scrapper
       /app
          main.py
          utils.py
          extract.py
       /data
          drama_list.csv

- main.py: Entry point for the script. Orchestrates the scraping process.
- utils.py: Contains utility functions for fetching pages and writing data to CSV.
- extract.py: Contains functions for extracting data from HTML pages.
- /data: Directory to store the output CSV file.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

