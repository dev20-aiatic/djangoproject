from django.urls import path
from .views import *

urlpatterns = [
    path('', helloword, name="Inicio"),
    path('', login, name="Inicio de sesión"),
]
