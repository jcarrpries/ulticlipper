from collections import defaultdict
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
    def to_representation(self, instance):
        tag_dict = defaultdict(list)
        for tag in instance.tag_set.all():
            tag_dict[tag.group.name].append(tag.name)

        return {
            "timestamp": instance.timestamp,
            "event_types": tag_dict["event_type"],
            "possession_types": tag_dict["possession_type"][0] if tag_dict["possession_type"] else None,
            "line_type": tag_dict["line_type"][0] if tag_dict["line_type"] else None,
            "passer": tag_dict["passer"][0] if tag_dict["passer"] else None,
            "receiver": tag_dict["receiver"][0] if tag_dict["receiver"] else None,
            "defender": tag_dict["defender"][0] if tag_dict["defender"] else None,
        }

    class Meta:
        model = Clip
        fields = ["timestamp", "event_types", "possession_types", "line_type", "passer", "receiver", "defender"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["timestamp", "text", "annotation"]
