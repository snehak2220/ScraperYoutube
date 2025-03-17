from django.db import models

class VideoScrape(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()  # Changed from video_url to url
    channel_name = models.CharField(max_length=100)
    views = models.CharField(max_length=20)
    time_posted = models.CharField(max_length=50)

    def __str__(self):
        return self.title
