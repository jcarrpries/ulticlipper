from rest_framework.test import APITestCase

from .models import Clip, Tag, TagGroup, Video

class ClipVideosTestCase(APITestCase):
    def setUp(self):
        # load some clips into the database for querying, with some tags
        video, _ = Video.objects.get_or_create(youtube_id='test', title='frisbee')
        clip, _ = Clip.objects.get_or_create(timestamp=0, duration=0, video=video)
        tag_group, _ = TagGroup.objects.get_or_create(name='event_type')
        tag, _ = Tag.objects.get_or_create(name='CATCH')
        tag_group.tags.add(tag)
        tag.clips.add(clip)
        
        clip, _ = Clip.objects.get_or_create(timestamp=1, duration=0, video=video)
        tag, _ = Tag.objects.get_or_create(name='DROP')
        tag_group.tags.add(tag)
        tag.clips.add(clip)

    def test_get_clips(self):
        video = Video.objects.get(title='frisbee')
        resp = self.client.get(f'/api/clips_by_video/{video.id}/')
        self.assertEqual(len(resp.data), 2)

        # Ensure event types are serialized correctly
        self.assertEqual(resp.data[0]['event_types'][0], 'CATCH')
        self.assertEqual(resp.data[1]['event_types'][0], 'DROP')
