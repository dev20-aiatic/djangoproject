from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

import website
from notes.views import *
from users.views import *
from website.views import Index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('users.urls')),
    path('app/notas/', include('notes.urls')),
    path('', include('website.urls')),
    path('app/', include('allauth.urls')),
    path('token', obtain_auth_token),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
