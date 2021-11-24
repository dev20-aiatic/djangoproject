from django.contrib.auth.decorators import login_required
from django.urls import path

from website.views import ReceivedView, ContactDelete, ContactDetail, ContactUpdate
from .views import *


urlpatterns = [
    path('notas/', login_required(BoardList.as_view()), name='boards'),
    path('notas/crear/', login_required(BoardCreate.as_view()), name='board-create'),
    path('notas/<uuid:id>/', login_required(BoardDetail.as_view()), name="board"),
    path('notas/<uuid:id>/actualizar/', login_required(BoardUpdate.as_view()), name='board-update'),
    path('notas/<uuid:id>/eliminar/', login_required(BoardDelete.as_view()), name='board-delete'),
    path('notas/<uuid:id>/crear-idea/', login_required(IdeaCreate.as_view()), name="ideas-create"),
    path('notas/<uuid:id>/<int:pk>/actualizar-idea', login_required(IdeaUpdate.as_view()), name="ideas-update"),
    path('notas/<uuid:id>/<int:pk>/borrar-idea/', login_required(IdeaDelete.as_view()), name="ideas-delete"),
    path('inbox/', login_required(ReceivedView.as_view()), name="inbox"),
    path('inbox/<int:pk>/', login_required(ContactDetail.as_view()), name="message"),
    path('inbox/<int:pk>/eliminar', ContactDelete.as_view(), name="message-delete"),
    path('inbox/<int:pk>/actualizar', ContactUpdate.as_view(), name="message-update"),
    path('boards', RestBoards.as_view(), name="boards-rest"),
    path('ideas', RestIdeas.as_view(), name="ideas"),
    path('create_idea', RestIdeaCreate.as_view(), name="idea-create"),


]
