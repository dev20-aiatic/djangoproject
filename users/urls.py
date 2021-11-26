from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import *

urlpatterns = [
    path('<str:username>/', login_required(ProfileDetail.as_view()), name="profile"),
    path('<str:username>/settings', login_required(ProfileEdit.as_view()), name="profile-edit"),
]
