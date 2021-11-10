from django.urls import path

from Practica_AIATIC import views
# from .views import *

urlpatterns = [
    path('', views.home, name="Inicio"),
    path('perfil/', views.profile, name="Perfil"),
    path('hello/', views.helloword, name="Hola mundo"),
    path('dev/', views.debug, name="Prueba"),

]
