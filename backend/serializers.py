from rest_framework import serializers
from backend.models import Clip, Video, ClipTags, Tag
import requests

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'youtube_id', 'title']

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'value']

class ClipSerializer(serializers.ModelSerializer):
    video = VideoSerializer()

    class Meta:
        model = Clip
        fields = ['id', 'timestamp', 'duration', 'created_at', 'video']

class ClipTagsSerializer(serializers.ModelSerializer):
    clip = ClipSerializer()
    tag = TagSerializer()

    class Meta:
        model = ClipTags
        fields = ['id', 'clip', 'tag']
