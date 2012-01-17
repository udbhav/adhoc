from django.db import models
from music.storage import SongStorage
from django.template.loader import render_to_string
from django.template import Context, Template

class Artist(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name

class MusicEmbed(models.Model):
    artist = models.ForeignKey(Artist)
    title = models.CharField(max_length=255)

    def __unicode__(self):
        return self.title

    def get_html(self):
        context = {}
        if hasattr(self, 'song'):
            context['song'] = self
        else:
            context['release'] = self

        return render_to_string('music/playlist.html', context)

class Song(MusicEmbed):
    song = models.FileField(upload_to='uploads/music', storage=SongStorage())
    track_number = models.IntegerField(null=True, blank=True)
    downloadable = models.BooleanField()

    def download_url(self):
        return self.file.storage.download_url(self.file.name)

class Release(MusicEmbed):
    songs = models.ManyToManyField(Song)
