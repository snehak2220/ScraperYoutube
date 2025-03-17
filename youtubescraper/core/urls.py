from django.urls import path
from . import views

urlpatterns = [
    path('scrape/', views.scrapeyoutube, name='scrape'),
    path('videos/', views.get_videos, name='get_videos'),
]