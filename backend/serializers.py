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

class BasicTagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		exclude = ["clips"]

class ClipSerializer(serializers.ModelSerializer):
    video = VideoSerializer()
	
    class Meta:
        model = Clip
        fields = "__all__"

class TagGroupSerializer(serializers.ModelSerializer):
	tags = BasicTagSerializer(many=True, read_only=True)

	class Meta:
		model = TagGroup
		fields = "__all__"

class TagClipSerializer(serializers.ModelSerializer):
    clips = ClipSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = "__all__"