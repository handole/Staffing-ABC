from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

from accounts.views import (login_view, register_view, logout_view)
from apps import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/', register_view, name='register'),
    url(r'^login/', login_view, name='login'), 
    url(r'^logout/', logout_view, name='logout'),

    url(r'^admin/', admin.site.urls),
    url(r'^', include('apps.urls', namespace='apps')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)