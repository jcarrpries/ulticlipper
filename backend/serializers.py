from rest_framework import serializers
from backend.models import Clip, Video
import requests

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'youtube_id', 'title']

class YoutubeIdField(serializers.RelatedField):
    def to_representation(self, value):
        return value.youtube_id

class ClipSerializer(serializers.ModelSerializer):
    video = VideoSerializer()

    class Meta:
        model = Clip
        fields = ['id', 'timestamp', 'duration', 'created_at', 'video']
