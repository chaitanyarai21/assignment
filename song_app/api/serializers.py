from rest_framework import serializers
from .models import Song, Podcast, AudioBook

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'name', 'duration', 'upload_time']

class PodcastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Podcast
        fields = ["id", "name", "duration", "upload_time", "hoster", "participants"]

class AudioBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioBook
        fields = ["id", "title", "author", "narrator", "duration", "upload_time"]