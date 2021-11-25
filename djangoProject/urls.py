from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

from notes.views import *
from users.views import *
from website.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('app/', include('notes.urls')),
    path('', include('website.urls')),
    path('auth/', include('allauth.urls')),
    path('token', obtain_auth_token),
    path('boards', RestBoards.as_view(), name="boards-rest"),
    path('ideas', RestIdeas.as_view(), name="ideas"),
    path('create_idea', RestIdeaCreate.as_view(), name="idea-create"),
    path('users', RestUsersList.as_view(), name="users"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
