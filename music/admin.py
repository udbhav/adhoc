from django.contrib import admin

from music.models import *

admin.site.register(Song)
admin.site.register(Artist)
admin.site.register(Release)

