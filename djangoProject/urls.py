from django.contrib import admin
from django.urls import path, include

from Practica_AIATIC import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('Practica_AIATIC.urls')),
    path('', views.login),
    path('accounts/', include('allauth.urls')),
]
