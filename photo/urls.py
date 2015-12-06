__author__ = 'vosoditdeus'
from django.conf.urls import patterns, include, url
from Ms import settings
from django.conf.urls.static import static
from photo.views import *

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'MySite2_7.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'addcomment/(?P<photo_id>\d)$', 'photo.views.addComment'),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT}),
                       url(r'preview/(?P<image_id>\d+)$', 'photo.views.Prewiew'),
                       url(r'album/(?P<album_id>\d+)$', 'photo.views.Albums'),
                       url(r'^about', 'photo.views.about'),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
