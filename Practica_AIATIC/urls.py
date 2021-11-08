from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="Inicio"),
    path('perfil/', profile, name="Perfil"),
    path('hello/', helloword, name="Hola mundo"),
]
