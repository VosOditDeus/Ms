__author__ = 'vosoditdeus'
from django.conf.urls import patterns, url
from Ms import settings,local_settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'MySite2_7.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^addlike/(?P<img_id>\d+)/$', 'photo.views.addlike', name='addlike'),
                       url(r'^addPhoto/', 'photo.views.addPhoto', name='addPhoto'),
                       url(r'yourpic/', 'photo.views.show_your_pictures', name='yourpic'),
                       url(r'image/(\d+)/$', 'photo.views.image', name='image'),
                       url(r'image/(\d+)/$', 'photo.views.image', name='image'),
                       url(r'image/(?P<id>\d+)/update/$', 'photo.views.update', name='update'),
                       url(r'image/(?P<id>\d+)/delete/$', 'photo.views.delete', name='delete'),
                       url(r'^cat_details/(?P<cat_pk>\d+)/$', 'photo.views.categories_detail',
name='cat_detail'),
                       # url(r'^multi/$','photo.views.multiuploader',name='multi')
                        )
if local_settings.DEBUG == "True":
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#TODO: Change it on deploy, read django docs