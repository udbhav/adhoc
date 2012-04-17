from django.contrib import admin
from django.contrib.flatpages.models import FlatPage

from blog.models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('embeds',)
    date_hierarchy = 'timestamp'
    list_display = ('title', 'timestamp', 'published')
    search_fields = ['title', 'slug']

    def queryset(self, request):
        qs = super(PostAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    class Media:
        css = {"all": ("css/admin.css",)}
        js = ("js/jquery.min.js","js/ckeditor/ckeditor.js","js/ckeditor/adapters/jquery.js","js/admin.js")

class TextEditorAdmin(admin.ModelAdmin):
    class Media:
        css = {"all": ("css/admin.css",)}
        js = ("js/jquery.min.js","js/ckeditor/ckeditor.js","js/ckeditor/adapters/jquery.js","js/admin.js")

admin.site.register(Post, PostAdmin)
admin.site.register(Image)
admin.site.register(Embed)
admin.site.register(AuthorProfile, TextEditorAdmin)
admin.site.register(Feature)
admin.site.register(Link)
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TextEditorAdmin)
