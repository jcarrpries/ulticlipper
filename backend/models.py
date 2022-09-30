from django.db import models

# Create your models here.
class Clip(models.Model):
    # youtube video ids are 11 characters
    vid_id = models.CharField(max_length=11)
    start = models.IntegerField()
    end = models.IntegerField()
