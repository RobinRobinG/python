from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='app_home'),
    #url(r'^add/$', add, name='add'),
    #url(r'^create/$', create, name='create'),
    #url(r'^destination/(?P<id>\d+)$', show, name='show'),
    #url(r'^join/(?P<id>\d+)$', jointrip, name='jointrip'),
]
