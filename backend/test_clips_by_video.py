from rest_framework.test import APITestCase

from .models import Clip, Tag, TagGroup, Video
from django.contrib.auth.models import User

class ClipVideosTestCase(APITestCase):
    def setUpAuth(self):
        resp = self.client.post('/api/createuser/', {
            "email": "user@gmail.com",
            "password": "password123",
            "display_name": "John",
        })

        self.client.post('/api/create_team/', {
            'team_name': 'Team A',
        })

        player_id = resp.json()['id']
        return player_id

    def setUp(self):
        player_id = self.setUpAuth()
        team = User.objects.get(id=player_id).user_data.active_team

        # load some clips into the database for querying, with some tags
        video, _ = Video.objects.get_or_create(youtube_id='test', title='frisbee', team=team)
        clip, _ = Clip.objects.get_or_create(timestamp=0, duration=0, video=video, team=team)
        tag_group, _ = TagGroup.objects.get_or_create(name='event_type', team=team)
        tag, _ = Tag.objects.get_or_create(name='CATCH', team=team)
        tag_group.tags.add(tag)
        tag.clips.add(clip)

        clip, _ = Clip.objects.get_or_create(timestamp=1, duration=0, video=video, team=team)
        tag, _ = Tag.objects.get_or_create(name='DROP', team=team)
        tag_group.tags.add(tag)
        tag.clips.add(clip)

    def test_get_clips(self):
        video = Video.objects.get(title='frisbee')
        resp = self.client.get(f'/api/clips_by_video/{video.id}/')
        self.assertEqual(len(resp.data), 2)

        # Ensure event types are serialized correctly
        self.assertEqual(resp.data[0]['event_types'][0], 'CATCH')
        self.assertEqual(resp.data[1]['event_types'][0], 'DROP')
