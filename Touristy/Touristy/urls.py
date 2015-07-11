from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Touristy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('home.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('login.urls')),
)
