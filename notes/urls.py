from django.contrib.auth.decorators import login_required
from django.urls import path

# from .views import *

from notes.views import BoardList, BoardCreate, BoardUpdate, BoardDelete

urlpatterns = [
    path('', login_required(BoardList.as_view()), name='boards'),
    path('crear/', login_required(BoardCreate.as_view()), name='board-create'),
    path('actualizar/<int:pk>/', login_required(BoardUpdate.as_view()), name='board-update'),
    path('eliminar/<int:pk>/', login_required(BoardDelete.as_view()), name='board-delete'),

]
