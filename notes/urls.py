from django.urls import path

# from .views import *

from notes.views import BoardList, BoardCreate, BoardUpdate, BoardDelete

urlpatterns = [
    path('', BoardList.as_view(), name='boards'),
    path('tablero-crear/', BoardCreate.as_view(), name='board-create'),
    path('tablero-actualizar/<str:pk>/', BoardUpdate.as_view(), name='board-update'),
    path('tablero-eliminar/<str:pk>/', BoardDelete.as_view(), name='board-delete'),

]
