from django.contrib import admin
from django.urls import path, include
from allauth.account import views as auth_views
from Practica_AIATIC import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('Practica_AIATIC.urls')),
    # path('', views.login),
    path('', auth_views.login, name="account_login"),
    path('', include('allauth.urls')),
]
