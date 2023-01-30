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
		fields = ["id", "name", "tags"]

class TagClipSerializer(serializers.ModelSerializer):
    clips = ClipSerializer(many=True, read_only=True)

    class Meta:
        model = Tag
        fields = "__all__"

class EventNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields=["name"]

class EventSerializer(serializers.ModelSerializer):
    event_types = serializers.SerializerMethodField()

    def get_event_types(self, clip):
        # Filter tags that belong to Tag Group Event
        event_tags = clip.tag_set.filter(group__name="event_type") # All event_type tags

        serializer = EventNameSerializer(event_tags, many=True)

        events = serializer.data
        return [event["name"] for event in events]

    class Meta:
        model = Clip
        fields = ["timestamp", "event_types"]
