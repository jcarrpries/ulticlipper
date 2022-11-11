from rest_framework import status
from rest_framework.test import APITestCase
from .sync_view import SyncUpload, SyncChooseGame, SyncCommit
from .test_data_helper import CSV_STRING
import tempfile

class SyncTestCase(APITestCase):
    def test_good_upload(self):
        f = tempfile.TemporaryFile()
        f.write(CSV_STRING)
        f.seek(0)
        resp = self.client.post('/api/sync/upload/', {'file': f})
        f.close()

        # test game should have 2 games in it
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(len(resp.data), 2)
    
    def test_bad_upload(self):
        # try csv file with nothing
        f = tempfile.TemporaryFile()
        f.write(b'this is not a csv file')
        f.seek(0)
        resp = self.client.post('/api/sync/upload/', {'file': f})
        f.close()

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
