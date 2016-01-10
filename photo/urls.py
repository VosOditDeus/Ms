__author__ = 'vosoditdeus'
from django.conf.urls import patterns, url
from Ms import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'MySite2_7.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r"^album/(?P<pk>\d)$", "photo.views.album", name='album'),
                       url(r'^addlike/(?P<img_id>\d+)/$','photo.views.addlike', name='addlike'),
                       url(r'^addPhoto/','photo.views.addPhoto', name='addPhoto'),
                       url(r'yourpic/','photo.views.show_your_pictures', name='youpic'),
                       url(r'image/(\d+)/$', 'photo.views.image', name='image'),
                       url(r'image/(\d+)/(full|edit)/$', 'photo.views.image', name='image'),
                       url(r'update/$','photo.views.update', name='update'),
                       url(r'^cat_details/(?P<cat_pk>\d+)/$','photo.views.categories_detail', name='cat_detail'),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
