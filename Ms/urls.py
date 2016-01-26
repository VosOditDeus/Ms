from django.conf.urls import patterns, include, url
from django.contrib import admin
from Ms import settings,local_settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'MySite2_7.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^photo/', include('photo.urls')),
                       url(r"^$", 'photo.views.God', name='God'),
                       url(r'^cus/$','photo.views.contact', name='Cus'),
                       url(r'^accounts/', include('registration.backends.default.urls')),
                       )
if local_settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#TODO: Change it on deploy, read django docs