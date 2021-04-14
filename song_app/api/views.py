from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import SongSerializer, PodcastSerializer, AudioBookSerializer
from .models import Song, Podcast, AudioBook
from rest_framework import status
import json
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone

# Create your views here.
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def welcome(request):
  content = { 'message': 'Welcome to audiobook store' }
  return JsonResponse(content, status=200)

@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def get_api(request, typee):
  payload = request.data
  if typee == "Song":
      songs = Song.objects.filter()
      serializer = SongSerializer(songs, many=True)
      return JsonResponse({'songs': serializer.data}, safe=False, status=status.HTTP_200_OK)

  if typee == "Podcast":
      podcasts = Podcast.objects.filter()
      serializer = PodcastSerializer(podcasts, many=True)
      return JsonResponse({'podcasts': serializer.data}, safe=False, status=status.HTTP_200_OK)

  if typee == "AudioBook":
      audiobooks = AudioBook.objects.filter()
      serializer = AudioBookSerializer(audiobooks, many=True)
      return JsonResponse({'audiobooks': serializer.data}, safe=False, status=status.HTTP_200_OK)



@api_view(["POST"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def add_api(request,typee):
    payload = request.data
    if typee == "Song":
        song = Song.objects.create(
            name = payload["name"],
            duration = payload["duration"],
            upload_time = timezone.now()
        )
        serializer = SongSerializer(song)
        print(serializer.data)
        return JsonResponse({"songs": serializer.data}, safe=False, status=status.HTTP_201_CREATED)

    if typee == "Podcast":
        podcast = Podcast.objects.create(
            name = payload["name"],
            duration = payload["duration"],
            upload_time = timezone.now(),
            hoster = payload["hoster"],
            participants = payload["participants"]
        )
        serializer = PodcastSerializer(podcast)
        print(serializer.data)
        return JsonResponse({"podcasts": serializer.data}, safe=False, status=status.HTTP_201_CREATED)

    if typee == "AudioBook":
        audiobook = AudioBook.objects.create(
            title = payload["title"],
            duration = payload["duration"],
            upload_time = timezone.now(),
            author = payload["author"],
            narrator = payload["narrator"]
        )
        serializer = AudioBookSerializer(audiobook)
        print(serializer.data)
        return JsonResponse({"audiobooks": serializer.data}, safe=False, status=status.HTTP_201_CREATED)

@api_view(["PUT"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def update_api(request, typee,song_id):
    payload = request.data
    if typee == "Song":
        try:
            song_item = Song.objects.filter(id=song_id)
            # returns 1 or 0
            song_item.update(**payload)
            song = Song.objects.get(id=song_id)
            serializer = SongSerializer(song)
            return JsonResponse({'song': serializer.data}, safe=False, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    if typee == "Podcast":
        try:
            podcast_item = Podcast.objects.filter(id=song_id)
            # returns 1 or 0
            podcast_item.update(**payload)
            podcast = Podcast.objects.get(id=song_id)
            serializer = PodcastSerializer(podcast)
            return JsonResponse({'podcast': serializer.data}, safe=False, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    if typee == "AudioBook":
        try:
            audiobook_item = AudioBook.objects.filter(id=song_id)
            # returns 1 or 0
            audiobook_item.update(**payload)
            audiobook = AudioBook.objects.get(id=song_id)
            serializer = AudioBookSerializer(audiobook)
            return JsonResponse({'audiobook': serializer.data}, safe=False, status=status.HTTP_200_OK)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_api(request, typee, song_id):
    if typee == "Song":
        try:
            song = Song.objects.get( id=song_id)
            song.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    


    if typee == "Podcast":
        try:
            podcast = Podcast.objects.get( id=song_id)
            podcast.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    


    if typee == "AudioBook":
        try:
            audiobook = AudioBook.objects.get( id=song_id)
            audiobook.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist as e:
            return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)    

