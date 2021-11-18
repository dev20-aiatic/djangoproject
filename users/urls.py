from django.contrib.auth.decorators import login_required
from django.urls import path

from users import views

# from .views import *


urlpatterns = [
    path('', views.home, name="Inicio"),
    path('perfil/<str:username>/', views.ProfileDetail.as_view(), name="Perfil"),
    path('edit/<str:username>/', login_required(views.ProfileEdit.as_view()), name="Perfil-Edit"),
    path('hello/', views.helloword, name="Hola mundo"),
    path('dev/', views.debug, name="Prueba"),
]
