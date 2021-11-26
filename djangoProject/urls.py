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
    path('profile/', include('users.urls')),
    path('app/', include('notes.urls')),
    path('', include('website.urls')),
    path('auth/', include('allauth.urls')),
    path('token', obtain_auth_token),
    path('boards', RestBoards.as_view(), name="boards-rest"),
    path('ideas', RestIdeas.as_view(), name="ideas"),
    path('create_idea', RestIdeas.as_view(), name="idea-create"),
    path('users', RestUsers.as_view(), name="users"),
    path('list', RestUsers.as_view(), name="users-list"),
    path('create_users', RestUsers.as_view(), name="users-import"),
    path('user/<int:pk>', RestGetUser.as_view(), name="user-detail"),
    path('create', RestUsers.as_view(), name="user-create"),
    path('delete/<int:pk>', RestDeleteUser.as_view(), name="user-delete"),


] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
