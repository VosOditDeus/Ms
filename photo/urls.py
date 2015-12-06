__author__ = 'vosoditdeus'
from django.conf.urls import patterns, url
from Ms import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'MySite2_7.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'addcomment/(?P<photo_id>\d)$', 'photo.views.addComment'),
                       (r'^media/(?P<path>.*)$', 'django.views.static.serve',
                        {'document_root': settings.MEDIA_ROOT}),
                       url(r"^album/(?P<pk>\d)$", "photo.views.album", name='album'),
                       url(r'^about', 'photo.views.about'),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
