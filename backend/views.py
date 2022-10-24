from django.http import Http404
from django.db import transaction
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import Clip, Video, Tag, TagGroup
from backend.serializers import ClipSerializer, TagSerializer, VideoSerializer, TagGroupSerializer

from backend.read_stats import get_point_clips
from backend.sync_view import youtube_id_from_url

import re
from datetime import datetime

# Create your views here.

# view for testing importing stats file
class TestStatsImport(APIView):
    def post(self, request, format=None):
        TEST_IMPORT_TITLE = 'test import please ignore'
        # delete previous imports
        old_import = Video.objects.filter(title__exact=TEST_IMPORT_TITLE)
        old_import.delete()

        csv_contents = request.data['file']
        url = request.data['url']
        game_date = datetime.fromisoformat(request.data['game_date'])
        tournament = request.data['tournament']
        opponent = request.data['opponent']
        video_offset = int(request.data['video_offset'])
        clips = get_point_clips(csv_contents, game_date, tournament, opponent, video_offset)

        video_id = youtube_id_from_url(url)
        new_video = Video(title=TEST_IMPORT_TITLE, youtube_id=video_id)
        with transaction.atomic():
            new_video.save()
            for clip in clips:
                new_clip = Clip(
                    timestamp=clip['timestamp'],
                    duration=clip['duration'],
                    video=new_video
                )
                new_clip.save()

        all_clips = Clip.objects.filter(video__exact=new_video)
        serializer = ClipSerializer(all_clips, many=True)
        vid_serializer = VideoSerializer(new_video)
        return Response({
            'video': vid_serializer.data,
            'clips': serializer.data,
        })

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
        clips = Clip.objects.all()
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
