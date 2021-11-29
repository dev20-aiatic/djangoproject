from django.contrib.auth.decorators import login_required
from django.urls import path

from website.views import ReceivedView, ContactDelete, ContactReply, ContactUpdate
from .views import *


urlpatterns = [
    path('home/', Dashboard.as_view(), name='dashboard'),
    path('boards/', login_required(BoardList.as_view()), name='boards'),
    path('board/add/', login_required(BoardCreate.as_view()), name='board-create'),
    path('board/<uuid:id>/', login_required(BoardDetail.as_view()), name="board"),
    path('board/<uuid:id>/edit/', login_required(BoardUpdate.as_view()), name='board-update'),
    path('board/<uuid:id>/delete/', login_required(BoardDelete.as_view()), name='board-delete'),
    path('board/<uuid:id>/add-idea/', login_required(IdeaCreate.as_view()), name="ideas-create"),
    path('board/<uuid:id>/<int:pk>/edit-idea', login_required(IdeaUpdate.as_view()), name="ideas-update"),
    path('notas/<uuid:id>/<int:pk>/delete-idea/', login_required(IdeaDelete.as_view()), name="ideas-delete"),
    path('inbox/', login_required(ReceivedView.as_view()), name="inbox"),
    path('inbox/<int:pk>/', login_required(ContactReply.as_view()), name="message"),
    path('inbox/<int:pk>/delete', ContactDelete.as_view(), name="message-delete"),
    path('inbox/<int:pk>/edit', ContactUpdate.as_view(), name="message-update"),

]
