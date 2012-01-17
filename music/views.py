import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from music.models import Song

@csrf_exempt
def play_song(request):
    error = False
    if request.is_ajax():
        if request.method == 'POST':
            song_ids = json.loads(request.POST['data'])
            songs = Song.objects.filter(id__in=song_ids)
            song_urls = {}
            for song in songs:
                song_urls[song.id] = song.song.url

            data = json.dumps(song_urls)
        else:
            error = True
    else:
        error = True

    if error:
        return HttpResponse('Invalid Request')
    else:
        mimetype = 'application/javascript'
        return HttpResponse(data,mimetype)
