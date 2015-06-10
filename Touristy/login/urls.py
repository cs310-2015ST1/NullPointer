__author__ = 'ch0l1n3'


from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
    url(r'^$', views.login_view, name='login'),
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$', views.userlogout, name='logout'),

)