from django.conf.urls.defaults import *

from advertising.views import *

urlpatterns = patterns(
    '',
    (r'^serve/$', serve, {}, 'serve_ads'),
)
