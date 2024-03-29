import time
from django.http import Http404
from django.db import transaction
from django.db.models import Q
from backend.auth_view import get_active_team
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Prefetch

from backend.models import (
    Clip,
    Video,
    Tag,
    TagGroup,
    Comment,
    UserData,
    Team,
    InviteCode,
)
from django.contrib.auth.models import User
from backend.serializers import (
    ClipSerializer,
    EventSerializer,
    TagClipSerializer,
    TagSerializer,
    VideoSerializer,
    TagGroupSerializer,
    EventSerializer,
    CommentSerializer,
    ClipTagSerializer,
)
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
            if tag_group.type == "numeric":
                min = request.GET.get(f"{tag_group_name}[min]", "")
                if min != "":
                    clips = clips.filter(
                        tag__group__name=tag_group_name, tag__value__gte=float(min)
                    )

                max = request.GET.get(f"{tag_group_name}[max]", "")
                if max != "":
                    clips = clips.filter(
                        tag__group__name=tag_group_name, tag__value__lte=float(max)
                    )

                next

            tag_ids_in_group = request.GET.get(tag_group_name, "[]")
            tag_ids_in_group = json.loads(tag_ids_in_group)

            if tag_ids_in_group and len(tag_ids_in_group) > 0:
                clips = clips.filter(tag__in=tag_ids_in_group)

        print("millis", round(time.time() * 1000) - start)
        serializer = ClipSerializer(clips, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        active_team = get_active_team(request)

        if active_team is None:
            return Response("no-active-team", status=400)

        video = Video.objects.filter(team=active_team).get(pk=request.data["video_id"])
        tag_ids = request.data["tag_ids"]
        tag_values = request.data["tag_values"]

        if video is None:
            return Response("no-video", status=400)
        new_clip = Clip(
            timestamp=request.data["timestamp"],
            duration=request.data["duration"],
            video=video,
            team=active_team,
            type="custom",
        )

        new_clip.save()
        if len(tag_ids) > 0:
            new_clip.tag_set.add(*tag_ids)

        for group_name, value in tag_values.items():
            if value == "":
                next
            group = TagGroup.objects.get(name=group_name)
            tag, _ = Tag.objects.get_or_create(
                group=group, type="numeric", value=float(value), name=value
            )
            new_clip.tag_set.add(tag)

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
        serializer = ClipTagSerializer(clip, context={"clip": clip})
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        active_team = get_active_team(request)
        if active_team is None:
            return Response("no-active-team", status=400)

        clip = self.get_object(pk, active_team)
        clip.delete()
        return Response("Clip deleted successfully", status=204)


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

        start_time = time.time()

        # Line 1: Query
        query_start = time.time()
        clips = (
            Clip.objects.select_related('team', 'video')
            .prefetch_related('tag_set__group')  # Add this line
            .filter(team=active_team, video=pk, type='generated')
        )
        query_end = time.time()

        # Line 2: Serialization
        serialization_start = time.time()
        serializer = EventSerializer(clips, many=True)
        serialization_end = time.time()

        # Line 3: Response
        response_start = time.time()
        response = Response(serializer.data)
        response_end = time.time()

        end_time = time.time()

        print("Time taken for query execution: ", query_end - query_start, " seconds")
        print("Time taken for serialization: ", serialization_end - serialization_start, " seconds")
        print("Time taken for creating response: ", response_end - response_start, " seconds")
        print("Total time taken for code execution: ", end_time - start_time, " seconds")

        return response


class CommentsByVideo(APIView):
    def get(self, request, pk):
        active_team = get_active_team(request)
        if active_team == None:
            return Response("no-active-team", status=400)

        comments = Comment.objects.filter(team=active_team).filter(video=pk)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)

    def post(self, request, pk, format=None):
        text = request.data["text"]
        timestamp = request.data["timestamp"]
        annotation = request.data["annotation"]
        video_id = int(request.data["video_id"])

        active_team = get_active_team(request)
        if active_team == None:
            return Response("no-active-team", status=400)

        video = Video.objects.filter(team=active_team).get(pk=video_id)

        new_comment = Comment(
            text=text,
            timestamp=timestamp,
            annotation=annotation,
            video=video,
            team=active_team,
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
        if settings.ENV_NAME[0] == "p":  # p for production, not allowed
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
