from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from allauth.account import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('users.urls')),
    path('notes/', include('notes.urls')),
    # path('', views.login),
    path('', auth_views.login, name="account_login"),
    path('', include('allauth.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
