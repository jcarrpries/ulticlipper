from rest_framework import serializers
from backend.models import Clip
import requests

class ClipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clip
        fields = ['id', 'vid_id', 'start', 'end']
    
    def validate_vid_id(self, value):
        if len(value) != 11:
            raise serializers.ValidationError('Invalid Video URL')
        return value
