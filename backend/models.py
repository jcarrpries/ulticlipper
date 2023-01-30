from django.db import models

# Create your models here.
class Video(models.Model):
    youtube_id = models.CharField(max_length=11)
    title = models.CharField(max_length=100)

class Clip(models.Model):
    timestamp = models.IntegerField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    date=models.DateTimeField(null=True)

    class Meta:
        ordering = ['timestamp']

class TagGroup(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        indexes = [models.Index(fields=['name']), ]

class Tag(models.Model):
    name = models.CharField(max_length=50)
    clips = models.ManyToManyField(Clip)
    group = models.ForeignKey(TagGroup, related_name='tags', on_delete=models.PROTECT, null=True)
    class Meta:
        indexes = [models.Index(fields=['name']), ]