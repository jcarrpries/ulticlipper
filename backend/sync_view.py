from django.db import transaction, IntegrityError
from django.utils.dateparse import parse_date

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import Clip, TagGroup, Video, Tag, TagGroup
from backend.stats_classes import EventType, Event

from pandas.errors import EmptyDataError

from backend.read_stats import get_team_data, get_point_clips, get_game_data, get_game_objects

from datetime import datetime
import re
import json

from backend.auth_view import get_active_team

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
        try:
            csv, unique_games = get_team_data(csv_file)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
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
        if youtube_id == '':
            return Response('Invalid youtube URL', status=status.HTTP_400_BAD_REQUEST)
        csv_file = request.data['file']
        game_date = datetime.fromisoformat(request.data['game_date'])
        tournament = request.data['tournament']
        opponent = request.data['opponent']
        clips = get_point_clips(csv_file, game_date, tournament, opponent, 0)
        csv_file.seek(0)
        csv, games = get_team_data(csv_file)
        game_data = get_game_data(csv, tournament, opponent, game_date, 0)
        game_object = get_game_objects(game_data)
        halftime = None

        # find halftime
        for idx, event in enumerate(game_object.events):
            if int(event.our_score) + int(event.their_score) == 8:
                # mark halftime as first event after halftime event
                halftime = game_object.events[idx+1].event_start_elapsed
            if event.event_type == EventType.HALFTIME:
                # mark halftime as first event after halftime event
                halftime = game_object.events[idx+1].event_start_elapsed
                break
        return Response({
            'youtube_id': youtube_id,
            'halftime': halftime,
            'clips': clips,
            'events': [event.serialize() for event in game_object.events]
        })

class SyncCommit(APIView):
    # get final list of clips to commit
    # return all good
    def post(self, request, format=None):
        new_clips = json.loads(request.data['clips'])
        new_events = json.loads(request.data['events'])
        url = request.data['url']
        game_date = datetime.fromisoformat(request.data['game_date'])
        tournament = request.data['tournament']
        opponent = request.data['opponent']

        active_team = get_active_team(request)
        if active_team == None:
            return Response("no-active-team", status=400)

        youtube_id = youtube_id_from_url(url)
        new_video = Video(title=f'{tournament} - vs. {opponent}, {str(game_date)}', youtube_id=youtube_id, team=active_team)
        try:
            with transaction.atomic():
                new_video.save()
                for i in range(len(new_events)):
                    event = new_events[i]
                    duration = new_events[i+1]['event_start_elapsed'] - event['event_start_elapsed'] if i < len(new_events) - 1 else 0
                    new_event = Clip(
                        timestamp=event['event_start_elapsed'],
                        date=parse_date(event['datetime_game']),
                        duration=duration,
                        video=new_video,
                        team=active_team
                    )
                    new_event.save()
                    for group, name in event.items():
                        ignore_fields = ['datetime_game', 'event_start_elapsed']
                        if group not in ignore_fields and name is not None and name != 'Anonymous':
                            tag_type = 'numeric' if group in Event.NUMERIC_FIELDS else 'text'
                            tag_group, _ = TagGroup.objects.get_or_create(name=group, team=active_team, type=tag_type)
                            if group == 'players_on':
                                for player_name in name:
                                    tag, _ = Tag.objects.get_or_create(name=player_name, group=tag_group, team=active_team)
                                    tag.clips.add(new_event)
                            else:
                                value = float(name) if tag_type == 'numeric' else None
                                tag, _ = Tag.objects.get_or_create(name=name, value=value, group=tag_group, team=active_team, type=tag_type)
                                tag.clips.add(new_event)

        except IntegrityError:
            return Response(status.HTTP_400_BAD_REQUEST)

        return Response(status.HTTP_201_CREATED)