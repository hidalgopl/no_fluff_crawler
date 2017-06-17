# Nofluffjobs webscraper
Scraper wrote to get data about latest job offers on http://nofluffjobs.com (hope they don't mind).
It scraps the data and dumps it to json file.


## Components:
- Selenium (for default Chrome webdriver is used)
  - to scrap the data from website
  
- BeautifulSoup
  - to parse data

## How to use:
- clone the repo
- `pip install -r requirements.txt`
- run  `main.py`
- Enjoy.

## Configuration
To scrap other data than Backend Python job offers, change variables in `sample_settings.py`
