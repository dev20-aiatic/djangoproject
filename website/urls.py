from django.urls import path
from allauth.account import views as allauth_views
from .views import *

urlpatterns = [
    path('', Index.as_view(), name="home"),
    path("nosotros/", About.as_view(), name="about"),
    path("servicios/", Services.as_view(), name="services"),
    path("contacto/", ContactCreate.as_view(), name="contact"),]
