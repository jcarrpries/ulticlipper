from rest_framework import serializers
from backend.models import Clip, Video, Tag, TagGroup

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"

class ClipSerializer(serializers.ModelSerializer):
    video = VideoSerializer()
	
    class Meta:
        model = Clip
        fields = "__all__"

class TagGroupSerializer(serializers.ModelSerializer):
	tags = TagSerializer(many=True, read_only=True)

	class Meta:
		model = TagGroup
		fields = "__all__"