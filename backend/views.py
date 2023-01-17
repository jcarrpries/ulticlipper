import time
from django.http import Http404
from django.db import transaction
from django.db.models import Q
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import Clip, Video, Tag, TagGroup
from backend.serializers import ClipSerializer, EventSerializer, TagClipSerializer, TagSerializer, VideoSerializer, TagGroupSerializer, EventSerializer
from django.conf import settings

from backend.read_stats import get_point_clips
from backend.sync_view import youtube_id_from_url

import re
import json
from datetime import datetime

# Create your views here.

class TagGroupList(APIView):
    def get(self, request, format=None):
        tag_groups = TagGroup.objects.all()
        serializer = TagGroupSerializer(tag_groups, many=True)
        return Response(serializer.data)

class TagList(APIView):
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)

class ClipList(APIView):
    def get(self, request, format=None):
        start = round(time.time() * 1000)
        clips = Clip.objects.all()
        
        tag_groups = TagGroup.objects.all()
        for tag_group in tag_groups:
            tag_group_name = tag_group.name
            tag_ids_in_group = request.GET.get(tag_group_name, '[]')
            tag_ids_in_group = json.loads(tag_ids_in_group)

            if(tag_ids_in_group and len(tag_ids_in_group) > 0):
                clips = clips.filter(tag__in=tag_ids_in_group)    
        print("millis", round(time.time() * 1000) - start)
        serializer = ClipSerializer(clips, many=True)
        return Response(serializer.data)
    
class ClipDetail(APIView):
    def get_object(self, pk):
        try:
            return Clip.objects.get(pk=pk)
        except Clip.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        clip = self.get_object(pk)
        serializer = ClipSerializer(clip)
        return Response(serializer.data)

class TagGroupDetail(APIView):
    def get_object(self, pk):
        try:
            return TagGroup.objects.get(pk=pk)
        except TagGroup.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        group = self.get_object(pk)
        serializer = TagGroupSerializer(group)
        return Response(serializer.data)

class TagDetail(APIView):
    def get_object(self, pk):
        try:
            return Tag.objects.get(pk=pk)
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        tag = self.get_object(pk)
        serializer = TagClipSerializer(tag)
        return Response(serializer.data)

class VideoList(APIView):
    def get(self, request, format=None):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
"""
Get clips within a video that a user might want to "Jump" to

Response Format:
[{
    "timestamp": 304,
    "event_types": [ "CATCH", "D"]
}, ...]

"""
class ClipsByVideo(APIView):
    def get(self, request, pk):
        clips = Clip.objects.filter(video=pk)
        serializer = EventSerializer(clips, many=True)

        return Response(serializer.data)

class HealthCheck(APIView):
    def get(self, request):
        return Response(status.HTTP_200_OK)

class ClearDatabase(APIView):
    # Test helper method for clearing database when testing
    def delete(self, request):
        if settings.ENV_NAME[0] == 'p': # p for production, not allowed
            return Response(status.HTTP_400_BAD_REQUEST)
        Clip.objects.all().delete()
        Video.objects.all().delete()
        TagGroup.objects.all().delete()
        Tag.objects.all().delete()
        return Response(status.HTTP_200_OK)
