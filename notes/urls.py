from django.contrib.auth.decorators import login_required
from django.urls import path

# from .views import *

from notes.views import BoardList, BoardCreate, BoardUpdate, BoardDelete, BoardDetail, IdeaCreate

urlpatterns = [
    path('', login_required(BoardList.as_view()), name='boards'),
    path('crear/', login_required(BoardCreate.as_view()), name='board-create'),
    path('<uuid:id>/', login_required(BoardDetail.as_view()), name="board"),
    path('<uuid:id>/crear-idea/', login_required(IdeaCreate.as_view()), name="ideas_create"),
    path('<uuid:id>/actualizar/', login_required(BoardUpdate.as_view()), name='board-update'),
    path('<uuid:id>/eliminar/', login_required(BoardDelete.as_view()), name='board-delete'),

]
