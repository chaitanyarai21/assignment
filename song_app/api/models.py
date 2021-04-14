from django.db import models

from django.conf import settings
from django.utils import timezone

# Create your models here.
class Song(models.Model):
  name = models.CharField(max_length=200)
  duration = models.IntegerField()
  upload_time = models.DateTimeField(default=timezone.now,blank=True)

  def __str__(self):
    return self.name

class Podcast(models.Model):
  name = models.CharField(max_length=100)
  duration = models.IntegerField()
  upload_time = models.DateTimeField(default=timezone.now)
  hoster = models.CharField(max_length=100)
  participants =models.CharField(max_length=100)
  
  def __str__(self):
    return self.title

class AudioBook(models.Model):
  title = models.CharField(max_length=200)
  author = models.CharField(max_length=200)
  narrator = models.CharField(max_length=200)
  duration = models.IntegerField()
  upload_time = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.title