# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Advertisement.paid'
        db.add_column('advertising_advertisement', 'paid', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Advertisement.active'
        db.add_column('advertising_advertisement', 'active', self.gf('django.db.models.fields.BooleanField')(default=False), keep_default=False)

        # Adding field 'Advertisement.paid_views'
        db.add_column('advertising_advertisement', 'paid_views', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)

        # Adding field 'Advertisement.views'
        db.add_column('advertising_advertisement', 'views', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Advertisement.paid'
        db.delete_column('advertising_advertisement', 'paid')

        # Deleting field 'Advertisement.active'
        db.delete_column('advertising_advertisement', 'active')

        # Deleting field 'Advertisement.paid_views'
        db.delete_column('advertising_advertisement', 'paid_views')

        # Deleting field 'Advertisement.views'
        db.delete_column('advertising_advertisement', 'views')


    models = {
        'advertising.advertisement': {
            'Meta': {'object_name': 'Advertisement'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'code': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateTimeField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'paid': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'paid_views': ('django.db.models.fields.IntegerField', [], {}),
            'position': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'start_date': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'views': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['advertising']
