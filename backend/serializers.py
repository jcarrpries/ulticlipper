from rest_framework import serializers
from backend.models import TestClip, Clip, Video
import requests

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'youtube_id', 'title']

class ClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clip
        fields = ['id', 'timestamp', 'duration', 'created_at', 'video_id']

class TestClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestClip
        fields = ['id', 'vid_id', 'start', 'end']
    
    def validate_vid_id(self, value):
        if len(value) != 11:
            raise serializers.ValidationError('Invalid Video URL')
        return value
