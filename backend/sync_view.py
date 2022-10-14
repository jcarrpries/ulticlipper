from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import Clip, Video
from backend.serializers import ClipSerializer, VideoSerializer

class SyncUpload(APIView):
    # get CSV
    # return list of games
    pass

class SyncChooseGame(APIView):
    # get game details (tourney, date, teams)
    # return clips for points
    # editing clips and synchronizing is handled in frontend
    pass

class SyncCommit(APIView):
    # get final list of clips to commit
    # return all good
    pass
