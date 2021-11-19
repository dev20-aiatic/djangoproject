from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from allauth.account import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from notes.views import *
from users.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('', include('notes.urls')),
    path('', include('allauth.urls')),
    path('token/', obtain_auth_token),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
