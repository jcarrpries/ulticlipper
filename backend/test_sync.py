from rest_framework import status
from rest_framework.test import APITestCase
from .sync_view import SyncUpload, SyncChooseGame, SyncCommit
from .test_data_helper import CSV_STRING
import tempfile

class SyncTestCase(APITestCase):
    def setUp(self):
        # Helper CSV file for adding to requests
        self.f = tempfile.TemporaryFile()
        self.f.write(CSV_STRING)
        self.f.seek(0)
    
    def tearDown(self):
        self.f.close()

    def test_good_upload(self):
        resp = self.client.post('/api/sync/upload/', {'file': self.f})

        # test game should have 2 games in it
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 2)
    
    def test_bad_upload(self):
        # try csv file with nothing
        self.f.write(b'this is not a csv file')
        self.f.seek(0)
        resp = self.client.post('/api/sync/upload/', {'file': self.f})

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_choose_game_good_url(self):
        resp = self.client.post('/api/sync/choosegame/', {
            'file': self.f,
            'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ',
            'game_date': '2019-06-22 19:03',
            'tournament': 'AUDL',
            'opponent': 'New York Empire'
        })

        self.assertEqual(resp.data['youtube_id'], 'dQw4w9WgXcQ')

    def test_choose_game_bad_url(self):
        resp = self.client.post('/api/sync/choosegame/', {
            'url': 'not a youtube URL'
        })

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

