from django.contrib import admin

from blog.models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('embeds',)

    class Media:
        css = {"all": ("css/admin.css",)}
        js = ("js/jquery.min.js","js/ckeditor/ckeditor.js","js/ckeditor/adapters/jquery.js","js/admin.js")


admin.site.register(Post, PostAdmin)
admin.site.register(Image)
admin.site.register(Embed)
admin.site.register(Feature)
