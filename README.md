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
## Installation
# 1. Clone the repository
 ```sh
   git clone https://github.com/snehak2220/ScraperYoutube.git
   cd ScraperYoutube
```
# 2. Create and activate a virtual environment
```sh
    python -m venv venv
    # For Windows
     venv\Scripts\activate
    # For macOS/Linux
    source venv/bin/activate
```
# 3.Install dependencies
```sh
   pip install -r requirements.txt
```
# 4. Install ChromeDriver
You will need to download ChromeDriver that corresponds to your version of Google Chrome. You can download it from here.

Make sure that ChromeDriver is either in your PATH or specify its path in the scrapeyoutube function of views.py.

# 5. Set up the Database
Run the following Django commands to set up the database:
```sh
 bash
 Copy
  python manage.py makemigrations
  python manage.py migrate
```sh
# 6. Start the Django Development Server
bash
Copy
```sh
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to access the web application.
```

