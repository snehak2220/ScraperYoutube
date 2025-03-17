from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
import time
from .models import VideoScrape
import logging
from rest_framework import viewsets
from .serializers import VideoSerializer

logger = logging.getLogger(__name__)

class VideoViewSet(viewsets.ModelViewSet):
    queryset = VideoScrape.objects.all()
    serializer_class = VideoSerializer

@api_view(['POST'])
def scrapeyoutube(request):
    try:
        search_query = request.data.get('query')
        if not search_query:
            return Response({"error": "No search query provided"}, status=400)

        VideoScrape.objects.all().delete()
        
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        driver = webdriver.Chrome(options=options)
        
        try:
            driver.get('https://www.youtube.com')
            time.sleep(2)

            search_box = driver.find_element(By.NAME, "search_query")
            search_box.send_keys(search_query)
            search_box.send_keys(Keys.RETURN)
            time.sleep(3)
            
            videos = driver.find_elements(By.CSS_SELECTOR, "ytd-video-renderer")
            video_data_list = []

            for video in videos[:5]:
                try:
                    video_data = {
                        'title': video.find_element(By.CSS_SELECTOR, "#video-title").text,
                        'url': video.find_element(By.CSS_SELECTOR, "#video-title").get_attribute("href"),
                        'channel_name': video.find_element(By.CSS_SELECTOR, "#channel-name").text,
                        'views': video.find_elements(By.CSS_SELECTOR, "#metadata-line span")[0].text,
                        'time_posted': video.find_elements(By.CSS_SELECTOR, "#metadata-line span")[1].text,
                    }
                    
                    video_obj = VideoScrape.objects.create(**video_data)
                    video_data['id'] = video_obj.id
                    video_data_list.append(video_data)

                except Exception as e:
                    logger.error(f"Error scraping video: {str(e)}")
                    continue

            return Response({
                "message": "Videos scraped successfully",
                "videos": video_data_list
            })

        finally:
            driver.quit()

    except Exception as e:
        logger.error(f"Scraping error: {str(e)}")
        return Response(
            {"error": "An error occurred while scraping videos"},
            status=500
        )

@api_view(['GET'])
def get_videos(request):
    try:
        videos = VideoScrape.objects.all().order_by('-id')
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"Error fetching videos: {str(e)}")
        return Response(
            {"error": "Failed to fetch videos"},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
