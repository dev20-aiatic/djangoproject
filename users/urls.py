from django.urls import path

from .views import *

urlpatterns = [
    path('<str:username>/', ProfileDetail.as_view(), name="profile"),
    path('<str:username>/settings', login_required(ProfileEdit.as_view()), name="profile-edit"),
]
