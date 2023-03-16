import time
from django.http import Http404
from django.db import transaction
from django.db.models import Q
from backend.auth_view import get_active_team
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import Clip, Video, Tag, TagGroup, Comment, UserData, Team, InviteCode
from django.contrib.auth.models import User
from backend.serializers import ClipSerializer, EventSerializer, TagClipSerializer, TagSerializer, VideoSerializer, TagGroupSerializer, EventSerializer, CommentSerializer
from django.conf import settings

from backend.read_stats import get_point_clips
from backend.sync_view import youtube_id_from_url

import re
import json
from datetime import datetime

# Create your views here.

class TagGroupList(APIView):
    def get(self, request, format=None):
        active_team = get_active_team(request)
        if active_team == None:
            return Response("no-active-team", status=400)

        tag_groups = TagGroup.objects.filter(team=active_team)
        serializer = TagGroupSerializer(tag_groups, many=True)
        return Response(serializer.data)

class TagList(APIView):
    def get(self, request, format=None):
        active_team = get_active_team(request)
        if active_team == None:
            return Response("no-active-team", status=400)

        tags = Tag.objects.filter(team=active_team)
        serializer = TagSerializer(tags, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        active_team = get_active_team(request)
        if active_team == None:
            return Response("no-active-team", status=400)

        name = request.data["name"]
        group_id = request.data["group_id"]

        group = TagGroup.objects.get(pk=group_id)
        new_tag = Tag(name=name, group=group, team=active_team)
        new_tag.save()
        serializer = TagSerializer(new_tag)
        return Response(serializer.data)


class ClipList(APIView):
    def get(self, request, format=None):

        active_team = get_active_team(request)
        if active_team is None:
            return Response("no-active-team", status=400)

        start = round(time.time() * 1000)
        clips = Clip.objects.filter(team=active_team)

        tag_groups = TagGroup.objects.filter(team=active_team)
        for tag_group in tag_groups:
            tag_group_name = tag_group.name
            tag_ids_in_group = request.GET.get(tag_group_name, '[]')
            tag_ids_in_group = json.loads(tag_ids_in_group)

            if(tag_ids_in_group and len(tag_ids_in_group) > 0):
                clips = clips.filter(tag__in=tag_ids_in_group)
        print("millis", round(time.time() * 1000) - start)
        serializer = ClipSerializer(clips, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        active_team = get_active_team(request)
        
        if active_team is None:
            return Response("no-active-team", status=400)
        
        video = Video.objects.filter(team=active_team).get(pk=request.data['video_id'])
        tag_ids = request.data['tag_ids']

        if video is None:
            return Response("no-video", status=400)
        new_clip = Clip(
            timestamp=request.data['timestamp'],
            duration=request.data['duration'],
            video=video,
            team=active_team
        )

        new_clip.save()
        if len(tag_ids) > 0:
            new_clip.tag_set.add(*tag_ids) 
            new_clip.save()
        
        serializer = ClipSerializer(new_clip)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ClipDetail(APIView):
    def get_object(self, pk, team):
        try:
            return Clip.objects.filter(team=team).get(pk=pk)
        except Clip.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        active_team = get_active_team(request)
        if active_team is None:
            return Response("no-active-team", status=400)

        clip = self.get_object(pk, active_team)
        serializer = ClipSerializer(clip)
        return Response(serializer.data)

class TagGroupDetail(APIView):
    def get_object(self, pk, active_team):
        try:
            return TagGroup.objects.filter(team=active_team).get(pk=pk)
        except TagGroup.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        active_team = get_active_team(request)
        if active_team == None:
            return Response("no-active-team", status=400)

        group = self.get_object(pk, active_team)
        serializer = TagGroupSerializer(group)
        return Response(serializer.data)

class TagDetail(APIView):
    def get_object(self, pk, active_team):
        try:
            return Tag.objects.filter(team=active_team).get(pk=pk)
        except Tag.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        active_team = get_active_team(request)
        if active_team == None:
            return Response("no-active-team", status=400)

        tag = self.get_object(pk, active_team)
        serializer = TagClipSerializer(tag)
        return Response(serializer.data)

class VideoList(APIView):
    def get(self, request, format=None):
        active_team = get_active_team(request)
        if active_team == None:
            return Response("no-active-team", status=400)

        videos = Video.objects.filter(team=active_team)
        serializer = VideoSerializer(videos, many=True)
        return Response(serializer.data)

class VideoDetail(APIView):
    def get(self, request, pk):
        active_team = get_active_team(request)
        if active_team == None:
            return Response("no-active-team", status=400)

        video = Video.objects.filter(team=active_team).get(pk=pk)
        serializer = VideoSerializer(video)
        return Response(serializer.data)

"""
Get clips within a video that a user might want to "Jump" to

Response Format:
[{
    "timestamp": 304,
    "event_types": [ "CATCH", "D"],
    "possession_type": "Offense"
}, ...]

"""
class ClipsByVideo(APIView):
    def get(self, request, pk):
        active_team = get_active_team(request)
        if active_team == None:
            return Response("no-active-team", status=400)

        clips = Clip.objects.filter(team=active_team).filter(video=pk)
        serializer = EventSerializer(clips, many=True)
        return Response(serializer.data)

class CommentsByVideo(APIView):
    def get(self, request, pk):
        active_team = get_active_team(request)
        if active_team == None:
            return Response("no-active-team", status=400)

        comments = Comment.objects.filter(team=active_team).filter(video=pk)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)

    def post(self, request, pk, format=None):
        text = request.data['text']
        timestamp = int(request.data['timestamp'])
        annotation = request.data['annotation']
        video_id = int(request.data['video_id'])

        active_team = get_active_team(request)
        if active_team == None:
            return Response("no-active-team", status=400)

        video = Video.objects.filter(team=active_team).get(pk=video_id)

        new_comment = Comment(
            text=text,
            timestamp=timestamp,
            annotation=annotation,
            video=video,
            team=active_team
        )
        new_comment.save()
        serializer = CommentSerializer(new_comment)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

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
        User.objects.all().delete()
        UserData.objects.all().delete()
        Team.objects.all().delete()
        InviteCode.objects.all().delete()

        return Response(status.HTTP_200_OK)
