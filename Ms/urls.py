from django.conf.urls import patterns, include, url
from django.contrib import admin
from Ms import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'MySite2_7.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       (r'^photo/', include('photo.urls')),
                       url(r'^login', 'photo.views.login',name='login'),
                       url(r'logout', 'photo.views.logout',name='logout'),
                       url(r"^$", 'photo.views.God',name='God'),
                       url(r'^accounts/', include('registration.backends.simple.urls')),
                       ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
