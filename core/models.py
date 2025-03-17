from django.db import models

# # Create your models here

class VideoScrape(models.Model):
    title = models.CharField(max_length=300) 
    url = models.URLField(unique=True)  
    channel_name = models.TextField(max_length=300)  
    views = models.TextField(max_length=50)
    time_posted = models.TextField(max_length=10)

    def __str__(self):
        return self.title
