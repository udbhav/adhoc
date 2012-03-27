from django.contrib import admin

from blog.models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('embeds',)

    def queryset(self, request):
        qs = super(PostAdmin, self).queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

    class Media:
        css = {"all": ("css/admin.css",)}
        js = ("js/jquery.min.js","js/ckeditor/ckeditor.js","js/ckeditor/adapters/jquery.js","js/admin.js")

class AuthorAdmin(admin.ModelAdmin):
    class Media:
        css = {"all": ("css/admin.css",)}
        js = ("js/jquery.min.js","js/ckeditor/ckeditor.js","js/ckeditor/adapters/jquery.js","js/admin.js")

admin.site.register(Post, PostAdmin)
admin.site.register(Image)
admin.site.register(Embed)
admin.site.register(AuthorProfile, AuthorAdmin)
admin.site.register(Feature)
admin.site.register(Link)
