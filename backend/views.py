from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from backend.models import Clip
from backend.serializers import ClipSerializer

import re


# Create your views here.
class ClipList(APIView):
    def get(self, request, format=None):
        clips = Clip.objects.all()
        serializer = ClipSerializer(clips, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        if 'url' in request.data:
            regex = re.compile('\?v=([a-zA-Z0-9_-]{11})')
            vid_id_matches = re.search(regex, request.data['url'])
            if vid_id_matches:
                request.data['vid_id'] = vid_id_matches.group(1)
            else:
                request.data['vid_id'] = ''

        serializer = ClipSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
    
    def delete(self, request, pk, format=None):
        clip = self.get_object(pk)
        clip.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
