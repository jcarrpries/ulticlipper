from rest_framework import serializers
from backend.models import Clip, Video, Tag, TagGroup, Comment

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
        exclude = ["clips", "group", "team", "type"]

class ClipSerializer(serializers.ModelSerializer):
    video = VideoSerializer()

    class Meta:
        model = Clip
        fields = "__all__"

class TagGroupSerializer(serializers.ModelSerializer):
    tags = BasicTagSerializer(many=True, read_only=True)

    class Meta:
        model = TagGroup
        fields = ["id", "name", "type", "tags"]

class TagGroupForClipSerializer(serializers.ModelSerializer):
    tags = serializers.SerializerMethodField()

    def get_tags(self, obj):
        clip = self.context.get('clip')
        tags = obj.tags.filter(clips=clip)
        return BasicTagSerializer(tags, many=True, read_only=True).data

    class Meta:
        model = TagGroup
        fields = ["id", "name", "type", "tags"]  

class ClipTagSerializer(serializers.ModelSerializer):
    tag_groups = TagGroupForClipSerializer(source='video.team.tag_groups', many=True, read_only=True)
    video = VideoSerializer()

    class Meta:
        model = Clip
        fields = "__all__"

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
    possession_types = serializers.SerializerMethodField()
    line_type = serializers.SerializerMethodField()
    passer = serializers.SerializerMethodField()
    receiver = serializers.SerializerMethodField()
    defender = serializers.SerializerMethodField()

    def get_event_types(self, clip):
        # Filter tags that belong to Tag Group Event
        event_tags = clip.tag_set.filter(group__name="event_type") # All event_type tags
        serializer = EventNameSerializer(event_tags, many=True)

        events = serializer.data
        return [event["name"] for event in events]

    def get_line_type(self, clip):
        # Filter tags that belong to Tag Group Event
        line_tags = clip.tag_set.filter(group__name="line_type") # All possession_type tags
        if len(line_tags) > 0:
            serializer = TagSerializer(line_tags, many=True)
            return serializer.data[0]["name"]
        else:
            return None

    def get_possession_types(self, clip):
        # Filter tags that belong to Tag Group Event
        possession_tags = clip.tag_set.filter(group__name="possession_type") # All possession_type tags

        if len(possession_tags) > 0:
            serializer = TagSerializer(possession_tags, many=True)
            return serializer.data[0]["name"]
        else:
            return None
    
    def get_passer(self, clip):
        passer_tags = clip.tag_set.filter(group__name="passer")
        if len(passer_tags) > 0:
            serializer = TagSerializer(passer_tags, many=True)
            return serializer.data[0]["name"]
        else:
            return None

    def get_receiver(self, clip):
        receiver_tags = clip.tag_set.filter(group__name="receiver")
        if len(receiver_tags) > 0:
            serializer = TagSerializer(receiver_tags, many=True)
            return serializer.data[0]["name"]
        else:
            return None
    def get_defender(self, clip):
        defender_tags = clip.tag_set.filter(group__name="defender")
        if len(defender_tags) > 0:
            serializer = TagSerializer(defender_tags, many=True)
            return serializer.data[0]["name"]
        else:
            return None
    class Meta:
        model = Clip
        fields = ["timestamp", "event_types", "possession_types", "line_type", "passer", "receiver", "defender"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["timestamp", "text", "annotation"]
