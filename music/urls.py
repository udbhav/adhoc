from django.conf.urls.defaults import *

urlpatterns = patterns(
    '',
    (r'^songs/play/$', 'music.views.play_song', {}, 'play_song'),
)
