# myapp/urls.py
from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import VideoViewSet

router = DefaultRouter()
router.register(r'videos', VideoViewSet)

urlpatterns = [
    path('', views.home, name='home'),
    path('api/', include(router.urls)),
    path('scrape/', views.scrapeyoutube, name='scrape_youtube'), 
    path('show_videos/', views.show_videos, name='show_videos'),
    
]