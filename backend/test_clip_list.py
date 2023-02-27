from rest_framework.test import APITestCase

from .models import Clip, Tag, TagGroup, Video
from django.contrib.auth.models import User

class ClipListTestCase(APITestCase):
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
        tag_group, _ = TagGroup.objects.get_or_create(name='players_on', team=team)
        tag, _ = Tag.objects.get_or_create(name='james', team=team)
        tag_group.tags.add(tag)
        tag.clips.add(clip)

        clip, _ = Clip.objects.get_or_create(timestamp=1, duration=1, video=video, team=team)

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

