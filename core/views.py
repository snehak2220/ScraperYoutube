from django.shortcuts import render,redirect
from django.http import HttpResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from .models import VideoScrape
import logging
from .models import VideoScrape
from rest_framework import viewsets
from .models import VideoScrape
from .serializers import VideoSerializer
import pandas as pd

class VideoViewSet(viewsets.ModelViewSet):
    queryset = VideoScrape.objects.all()
    serializer_class = VideoSerializer
def home(request):
    return render(request,'index.html')
# Set up logging
logger = logging.getLogger(__name__)

def scrapeyoutube(request):
    if request.method == 'POST':
        search_query = request.POST.get('query', '')
        if not search_query:
            return HttpResponse("No search query provided.")

        logger.info(f"Entered search query: {search_query}")
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(options=options)
        driver.get('https://www.youtube.com')

        try:
            search_box = driver.find_element(By.CLASS_NAME, "ytSearchboxComponentInput")
            search_box.send_keys(search_query)
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)
            video_data_list = []

            for i in range(1, 5):  
                try:
                    video_element = driver.find_element(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]')
                    video_url = video_element.find_element(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[1]/div/h3/a').get_attribute('href')
                    video_title = video_element.find_element(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[1]/div/h3/a/yt-formatted-string').text
                    video_views = video_element.find_element(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[1]').text
                    video_time = video_element.find_element(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[1]/ytd-video-meta-block/div[1]/div[2]/span[2]').text
                    channel_name = video_element.find_element(By.XPATH, f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[2]/ytd-channel-name/div/div/yt-formatted-string/a').text
                    

                    video = VideoScrape.objects.create(
                        title=video_title,
                        url=video_url,
                        views=video_views,
                        time_posted=video_time,
                        channel_name=channel_name
                    )
                    video.save()
                    
                    video_data_list.append({
                        'title': video_title,
                        'video_url': video_url,
                        'views': video_views,
                        'time_posted': video_time,
                        'channel_name': channel_name,
                        
                    
                    })
                    print(".......................................video data list..............................................")
                    print(video_data_list)

                    logger.info(f"Video {i}: {video_title} - {video_views} views")

                except Exception as e:
                    logger.error(f"Error scraping video {i}: {e}")

            # Delay to make sure the browser is done processing
            time.sleep(5)

            # Quit the driver after scraping is done
            driver.quit()
            df = pd.DataFrame(video_data_list)

            # Save the DataFrame to an Excel file
            df.to_excel('scraped_videos.xlsx', index=False)

            # Optional: Store the file path in session or database if needed
            request.session['video_data_list'] = video_data_list  # Storing in session
            return redirect('show_videos')  
            # Return the success response
            

        except Exception as e:
            logger.error(f"Error during scraping: {e}")
            return HttpResponse("An error occurred during scraping.")

    return HttpResponse("Invalid request.")

def show_videos(request):
    # Retrieve video data from the session
    video_data_list = request.session.get('video_data_list', [])
    
    # Pass the data to the template
    return render(request, 'show_videos.html', {'videos': video_data_list})
