from django.urls import path
from .views import *

urlpatterns = [
    path('perfil/<str:username>/', ProfileDetail.as_view(), name="Perfil"),
    path('edit/<str:username>/', login_required(ProfileEdit.as_view()), name="Perfil-Edit"),
    path('users', RestUsersList.as_view(), name="users"),
]
