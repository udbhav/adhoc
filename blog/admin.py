from django.contrib import admin
from django.contrib.flatpages.models import FlatPage

from blog.models import *

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('embeds',)
    date_hierarchy = 'timestamp'
    list_display = ('title', 'timestamp', 'published')
    search_fields = ['title', 'slug']
    exclude = None
    _exclude = exclude

    def queryset(self, request):
        qs = super(PostAdmin, self).queryset(request)
        if request.user.is_superuser or request.user.has_perm('blog.view_all_posts'):
            return qs
        return qs.filter(author=request.user)

    def allowed_to_publish(self, user):
        allowed = False
        if user.is_superuser:
            allowed = True
        else:
            if user.has_perm('blog.publish_post'):
                allowed = True

        return allowed

    def change_view(self, request, extra_context=None):
        if not self.allowed_to_publish(request.user):
            self.exclude = ('published',)
        else:
            self.exclude = self._exclude
        return super(PostAdmin, self).change_view(request, extra_context)

    def add_view(self, request, extra_context=None):
        if not self.allowed_to_publish(request.user):
            self.exclude = ('published',)
        else:
            self.exclude = self._exclude
        return super(PostAdmin, self).add_view(request, extra_context)

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
