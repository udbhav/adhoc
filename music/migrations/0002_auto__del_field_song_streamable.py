# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'Song.streamable'
        db.delete_column('music_song', 'streamable')


    def backwards(self, orm):
        
        # Adding field 'Song.streamable'
        db.add_column('music_song', 'streamable', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)


    models = {
        'music.artist': {
            'Meta': {'object_name': 'Artist'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'music.musicembed': {
            'Meta': {'object_name': 'MusicEmbed'},
            'artist': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['music.Artist']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'music.release': {
            'Meta': {'object_name': 'Release', '_ormbases': ['music.MusicEmbed']},
            'musicembed_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['music.MusicEmbed']", 'unique': 'True', 'primary_key': 'True'}),
            'songs': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['music.Song']", 'symmetrical': 'False'})
        },
        'music.song': {
            'Meta': {'object_name': 'Song', '_ormbases': ['music.MusicEmbed']},
            'downloadable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'musicembed_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['music.MusicEmbed']", 'unique': 'True', 'primary_key': 'True'}),
            'song': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'track_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['music']
