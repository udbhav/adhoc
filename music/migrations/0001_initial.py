# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Artist'
        db.create_table('music_artist', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('music', ['Artist'])

        # Adding model 'MusicEmbed'
        db.create_table('music_musicembed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('artist', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['music.Artist'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('music', ['MusicEmbed'])

        # Adding model 'Song'
        db.create_table('music_song', (
            ('musicembed_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['music.MusicEmbed'], unique=True, primary_key=True)),
            ('song', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('track_number', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('streamable', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('downloadable', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('music', ['Song'])

        # Adding model 'Release'
        db.create_table('music_release', (
            ('musicembed_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['music.MusicEmbed'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('music', ['Release'])

        # Adding M2M table for field songs on 'Release'
        db.create_table('music_release_songs', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('release', models.ForeignKey(orm['music.release'], null=False)),
            ('song', models.ForeignKey(orm['music.song'], null=False))
        ))
        db.create_unique('music_release_songs', ['release_id', 'song_id'])


    def backwards(self, orm):
        
        # Deleting model 'Artist'
        db.delete_table('music_artist')

        # Deleting model 'MusicEmbed'
        db.delete_table('music_musicembed')

        # Deleting model 'Song'
        db.delete_table('music_song')

        # Deleting model 'Release'
        db.delete_table('music_release')

        # Removing M2M table for field songs on 'Release'
        db.delete_table('music_release_songs')


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
            'streamable': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'track_number': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['music']
