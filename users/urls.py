from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('dashboard/', views.home, name='dashboard'),
    path('perfil/<str:username>/', ProfileDetail.as_view(), name="profile"),
    path('edit/<str:username>/', login_required(ProfileEdit.as_view()), name="profile-edit"),
    path('users', RestUsersList.as_view(), name="users"),
]
