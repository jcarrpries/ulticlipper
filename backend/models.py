from django.db import models

# Create your models here.
class TestClip(models.Model):
    # youtube video ids are 11 characters
    vid_id = models.CharField(max_length=11)
    start = models.IntegerField()
    end = models.IntegerField()

class Video(models.Model):
    youtube_id = models.CharField(max_length=11)
    title = models.CharField(max_length=100)

class Clip(models.Model):
    timestamp = models.IntegerField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    value = models.CharField(max_length=50)

class ClipTags(models.Model):
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
