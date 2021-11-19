from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import *


urlpatterns = [
    path('', login_required(BoardList.as_view()), name='boards'),
    path('crear/', login_required(BoardCreate.as_view()), name='board-create'),
    path('<uuid:id>/', login_required(BoardDetail.as_view()), name="board"),
    path('<uuid:id>/actualizar/', login_required(BoardUpdate.as_view()), name='board-update'),
    path('<uuid:id>/eliminar/', login_required(BoardDelete.as_view()), name='board-delete'),
    path('<uuid:id>/crear-idea/', login_required(IdeaCreate.as_view()), name="ideas-create"),
    path('<uuid:id>/<int:pk>/actualizar-idea', login_required(IdeaUpdate.as_view()), name="ideas-update"),
    path('<uuid:id>/<int:pk>/borrar-idea/', login_required(IdeaDelete.as_view()), name="ideas-delete"),
    path('boards', RestBoards.as_view(), name="boards-rest"),
    path('ideas', RestIdeas.as_view(), name="ideas"),
    path('create_idea', RestIdeaCreate.as_view(), name="idea-create"),


]
