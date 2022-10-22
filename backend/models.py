from django.db import models

# Create your models here.
class Video(models.Model):
    youtube_id = models.CharField(max_length=11, unique=True)
    title = models.CharField(max_length=100)

class Clip(models.Model):
    timestamp = models.IntegerField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    class Meta:
        ordering = ['timestamp']

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    value = models.CharField(max_length=50)
    clips = models.ManyToManyField(Clip)
	
    class Meta:
        indexes = [models.Index(fields=['name']), ]

class ClipTags(models.Model):
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE, related_name='cliptags')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

class TagGroup(models.Model):
    name = models.CharField(max_length=50, unique=True)
    tags = models.ManyToManyField(Tag)
    
    class Meta:
        indexes = [models.Index(fields=['name']), ]