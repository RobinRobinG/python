from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.belt.urls', namespace='home')),
    url(r'^login/', include('apps.login.urls', namespace='login')),
]

