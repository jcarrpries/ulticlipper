from rest_framework.test import APITestCase

from .models import Clip, Tag, TagGroup, Video

class ClipListTestCase(APITestCase):
    def setUp(self):
        # load some clips into the database for querying, with some tags
        video, _ = Video.objects.get_or_create(youtube_id='test', title='frisbee')
        clip, _ = Clip.objects.get_or_create(timestamp=0, duration=0, video=video)
        tag_group, _ = TagGroup.objects.get_or_create(name='players_on')
        tag, _ = Tag.objects.get_or_create(name='james')
        tag_group.tags.add(tag)
        tag.clips.add(clip)
        
        clip, _ = Clip.objects.get_or_create(timestamp=1, duration=1, video=video)

    def test_no_params(self):
        resp = self.client.get('/api/clips/?')
        self.assertEqual(len(resp.data), 2)
    
    def test_param(self):
        james_tag = Tag.objects.get(name='james')
        resp = self.client.get(f'/api/clips/?players_on=[{james_tag.id}]&')
        self.assertEqual(len(resp.data), 1)
    
    def test_no_clips_found(self):
        resp=self.client.get(f'/api/clips/?players_on=[99]&')
        self.assertEqual(len(resp.data), 0)

