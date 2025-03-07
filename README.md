# ScraperYoutube
This is a Django-based web application that uses Selenium to scrape YouTube video data based on a search query. The data includes the video title, URL, views, time posted, and the channel name. The scraped data is stored in the database and can be downloaded as an Excel file.
# Features
Scrape YouTube: Enter a search query and the app scrapes video information from YouTube.
Data Storage: Scraped video data is stored in the database.
Excel Export: The scraped video data can be exported to an Excel file.
Display Data: The scraped videos are displayed on a web page.
# Requirements
- Python 3.x
- Django 3.x or higher
- Selenium
- ChromeDriver (make sure it matches your version of Chrome)
- Pandas
- openpyxl (for saving to Excel)
Installation
1. Clone the repository
 ```sh
   git clone https://github.com/snehak2220/ScraperYoutube.git
    cd ScraperYoutube
```
