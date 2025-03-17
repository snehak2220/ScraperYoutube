from rest_framework import serializers
from .models import VideoScrape

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoScrape
        fields = '__all__'