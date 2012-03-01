# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Advertisement.code'
        db.add_column('advertising_advertisement', 'code', self.gf('django.db.models.fields.TextField')(default='', blank=True), keep_default=False)

        # Changing field 'Advertisement.image'
        db.alter_column('advertising_advertisement', 'image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # Deleting field 'Advertisement.code'
        db.delete_column('advertising_advertisement', 'code')

        # Changing field 'Advertisement.image'
        db.alter_column('advertising_advertisement', 'image', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))


    models = {
        'advertising.advertisement': {
            'Meta': {'object_name': 'Advertisement'},
            'code': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['advertising']
