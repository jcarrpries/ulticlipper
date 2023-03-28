from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField(User, related_name='teams')

class UserData(models.Model): # Extra data about users that can't be stored in the built-in User model
    user = models.OneToOneField(User, related_name='user_data', on_delete=models.CASCADE)
    active_team = models.ForeignKey(Team, related_name='active_users', on_delete=models.SET_NULL, null=True)

class Video(models.Model):
    youtube_id = models.CharField(max_length=11)
    title = models.CharField(max_length=100)
    team = models.ForeignKey(Team, related_name='videos', on_delete=models.CASCADE, null=True)

class Clip(models.Model):
    timestamp = models.IntegerField()
    duration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    date=models.DateTimeField(null=True)
    team = models.ForeignKey(Team, related_name='clips', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['timestamp']

class TagGroup(models.Model):
    TYPES = (
        ('text', 'Text'),
        ('numeric', 'Numeric')
    )
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, related_name='tag_groups', on_delete=models.CASCADE, null=True)
    type = models.CharField(choices=TYPES, max_length=20, default='text')

    class Meta:
        indexes = [models.Index(fields=['name']), ]

class Tag(models.Model):
    TYPES = (
        ('text', 'Text'),
        ('numeric', 'Numeric')
    )
    name = models.CharField(max_length=50, null=True)
    value = models.FloatField(null=True)
    clips = models.ManyToManyField(Clip)
    group = models.ForeignKey(TagGroup, related_name='tags', on_delete=models.PROTECT, null=True)
    team = models.ForeignKey(Team, related_name='tags', on_delete=models.CASCADE, null=True)
    type = models.CharField(choices=TYPES, max_length=20, default='text')

    def save(self, *args, **kwargs):
        if self.type != self.group.type:
            raise ValueError('Tag type must match TagGroup type')
        if self.name is None and self.value is None:
            raise ValueError("Either name or value must have a value")
        
        super().save(*args, **kwargs)

    class Meta:
        indexes = [models.Index(fields=['name']), ]


class InviteCode(models.Model): # One-time code to invite user to team
    code = models.CharField(max_length=50)
    team = models.ForeignKey(Team, related_name='active_codes', on_delete=models.CASCADE, null=True)

class Comment(models.Model):
    text = models.CharField(max_length=280)
    timestamp = models.FloatField()
    annotation = models.CharField(max_length=65000)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, related_name='comments', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['timestamp']

