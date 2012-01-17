from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required, permission_required

from blog.views import *

urlpatterns = patterns(
    '',
    (r'^images/$', login_required(ImageList.as_view()), {}, 'images'),
    (r'^images/new/$', new_image, {}, 'new_image'),
    (r'^tag/(?P<tag>[-\w]+)/$', PostsByTag.as_view(), {}, 'posts_by_tag'),
    (r'^(?P<slug>[-\w]+)/$', PostDetail.as_view(), {}, 'post'),
    (r'^$', PostIndex.as_view(), {}, 'home'),
)
