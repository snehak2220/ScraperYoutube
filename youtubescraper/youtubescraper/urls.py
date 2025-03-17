from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('videos/', csrf_exempt(views.get_videos), name='get_videos'),
    path('scrape/', csrf_exempt(views.scrapeyoutube), name='scrape'),
]
