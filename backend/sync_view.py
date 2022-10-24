from django.db import transaction, IntegrityError

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import Clip, TagGroup, Video, Tag, TagGroup
from backend.stats_classes import EventType

from backend.read_stats import get_team_data, get_point_clips, get_game_data, get_game_objects

from datetime import datetime
import re
import json

def youtube_id_from_url(url):
    regex = re.compile('\?v=([a-zA-Z0-9_-]{11})')
    vid_id_matches = re.search(regex, url)
    if vid_id_matches:
        return vid_id_matches.group(1)
    return ''

class SyncUpload(APIView):
    # get CSV
    # return list of games
    def post(self, request, format=None):
        csv_file = request.data['file']
        csv, unique_games = get_team_data(csv_file)
        resp = []
        for game in unique_games:
            game_date, tournament, opponent = game
            resp.append({
                'game_date': game_date,
                'tournament': tournament,
                'opponent': opponent,
            })
        return Response(resp)

class SyncChooseGame(APIView):
    # get game details (tourney, date, teams)
    # return clips for points and halves
    # editing clips and synchronizing is handled in frontend
    def post(self, request, format=None):
        youtube_id = youtube_id_from_url(request.data['url'])
        csv_file = request.data['file']
        game_date = datetime.fromisoformat(request.data['game_date'])
        tournament = request.data['tournament']
        opponent = request.data['opponent']
        clips = get_point_clips(csv_file, game_date, tournament, opponent, 0)
        csv_file.seek(0)
        csv, games = get_team_data(csv_file)
        game_data = get_game_data(csv, tournament, opponent, game_date, 0)
        game_object = get_game_objects(game_data)
        for idx, event in enumerate(game_object.events):
            if event.event_type == EventType.HALFTIME:
                # mark halftime as first event after halftime event
                halftime = game_object.events[idx+1].event_start_elapsed
        return Response({
            'youtube_id': youtube_id,
            'halftime': halftime,
            'clips': clips,
        })

class SyncCommit(APIView):
    # get final list of clips to commit
    # return all good
    def post(self, request, format=None):
        new_clips = json.loads(request.data['clips'])
        url = request.data['url']
        game_date = datetime.fromisoformat(request.data['game_date'])
        tournament = request.data['tournament']
        opponent = request.data['opponent']

        youtube_id = youtube_id_from_url(url)
        new_video = Video(title=f'{tournament} - vs. {opponent}, {str(game_date)}', youtube_id=youtube_id)
        try:
            with transaction.atomic():
                new_video.save()
                for clip in new_clips:
                    new_clip = Clip(
                        timestamp=clip['timestamp'],
                        duration=clip['duration'],
                        video=new_video
                    )
                    new_clip.save()
                    for tagGroup, tagName in clip['tags'].items():
                        tag_group, _ = TagGroup.objects.get_or_create(name=tagGroup)
                        tag, created = Tag.objects.get_or_create(name=tagName)
                        tag_group.tags.add(tag)
                        tag.clips.add(new_clip)
    
        except IntegrityError:
            return Response(status.HTTP_400_BAD_REQUEST)
        
        return Response(status.HTTP_201_CREATED)