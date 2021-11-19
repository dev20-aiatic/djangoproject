from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from rest_framework import generics, permissions

from .forms import NewBoard, NewIdea
from .models import Ideas, Board

# RestFramework Views
from .serializers import BoardsSerializer, IdeasSerializer, IdeaCreateSerializer


class RestBoards(generics.ListCreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardsSerializer
    permission_classes = [permissions.AllowAny]


class RestIdeas(generics.ListAPIView):
    queryset = Ideas.objects.all()
    serializer_class = IdeasSerializer
    permission_classes = [permissions.AllowAny]


class RestIdeaCreate(generics.CreateAPIView):
    serializer_class = IdeaCreateSerializer
    permission_classes = [permissions.AllowAny]


# Board's Views

class BoardList(ListView):
    model = Board
    template_name = 'notes/board_list.html'
    context_object_name = 'board'
    ordering = ['-updated_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all'] = Board.objects.all()
        context['public_list'] = Board.objects.filter(status='publico')
        context['private_list'] = Board.objects.filter(status='privado')
        context['my_boards'] = Board.objects.filter(user=self.request.user.id)
        return context


class BoardCreate(CreateView):
    model = Board
    form_class = NewBoard
    template_name = 'notes/board_create.html'
    success_url = '/notes/crear/'

    def get_object(self, queryset=None):
        return Board.objects.get(id=self.kwargs.get("id"))

    def get_success_url(self):
        return reverse('boards')

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial()
        initial['user'] = self.request.user
        return initial

    def form_valid(self, form):
        messages.success(self.request, f"¡Tablero creado correctamente!")
        return super().form_valid(form)


class BoardDetail(DetailView):
    model = Board
    context_object_name = 'board'
    template_name = 'notes/board_detail.html'

    def get_object(self, queryset=None):
        return Board.objects.get(id=self.kwargs.get("id"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ideas'] = Ideas.objects.filter(board=self.kwargs.get('id'))

        return context


class BoardUpdate(UpdateView):
    model = Board
    template_name = 'notes/board_update.html'
    fields = ('name', 'status')
    context_object_name = 'board'
    success_url = '/'
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return reverse('boards')

    def form_valid(self, form):
        board_object = Board.objects.get(id=self.kwargs.get('id'))

        if board_object.user == self.request.user:
            messages.success(
                self.request, f"¡Tablero modificar exitosamente!")
            return super().form_valid(form)
        else:
            messages.error(
                self.request, f"No tienes permiso para modificar este tablero")
            return super().form_invalid(form)


class BoardDelete(DeleteView):
    model = Board
    context_object_name = 'board'
    template_name = 'notes/board_delete.html'
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return reverse('boards')

    def delete(self, request, *args, **kwargs):
        board_object = Board.objects.get(id=self.kwargs.get('id'))

        if board_object.user == self.request.user:
            messages.error(
                self.request, f"Tablero borrado exitosamente")
            return super(BoardDelete, self).delete(
                request, *args, **kwargs)
        else:
            messages.error(
                self.request, f"No tienes permisos para borrar este tablero")
            return redirect(reverse('board', kwargs={'id': self.kwargs.get('id')}))

    def get_success_url(self):
        return reverse('boards')


# Ideas' Views

class IdeaCreate(CreateView):
    model = Ideas
    form_class = NewIdea
    context_object_name = 'ideas'
    template_name = 'notes/ideas_create.html'
    success_url = reverse_lazy('boards_id')
    pk = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['board'] = Board.objects.get(id=self.kwargs.get('id'))
        return context

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial()
        initial['user'] = self.request.user
        initial['board'] = Board.objects.get(id=self.kwargs.get('id'))
        return initial

    def form_valid(self, form):
        board_object = Board.objects.get(id=self.kwargs.get('id'))

        if board_object.status == 'o':
            messages.success(
                self.request, f"¡Idea añadida correctamente!")
            self.pk = self.kwargs.get('pk')
            return super().form_valid(form)
        else:
            if str(board_object.user) == str(self.request.user):
                messages.success(
                    self.request, f"Idea añadida correctamente!")
                self.pk = self.kwargs.get('pk')
                return super().form_valid(form)
            else:
                messages.error(
                    self.request, f"No tienes permisos para añadir notas en este tablero")
                form.add_error(
                    field="user", error="No tienes permisos para añadir notas en este tablero")
                return super().form_invalid(form)

    def get_success_url(self):
        return reverse('board', kwargs={'id': self.kwargs.get("id")})


class IdeaUpdate(UpdateView):
    model = Ideas
    context_object_name = 'ideas'
    fields = ('title', 'content')
    template_name = 'notes/ideas_update.html'
    success_url = reverse_lazy('boards_id')
    pk = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['board'] = Board.objects.get(id=self.kwargs.get('id'))
        context['idea'] = Ideas.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('board', kwargs={'id': self.kwargs.get('id')}))

    def form_valid(self, form):
        board_object = Board.objects.get(id=self.kwargs.get('id'))
        idea_object = Ideas.objects.get(pk=self.kwargs.get('pk'))

        if board_object.user == self.request.user and idea_object.user == self.request.user:
            messages.success(
                self.request, f"¡Idea modificada exitosamente!")
            return super().form_valid(form)
        else:
            messages.error(
                self.request, f"No tienes permiso para modificar este tablero")
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('board', kwargs={'id': self.kwargs.get("id")})


class IdeaDelete(DeleteView):
    model = Ideas
    fields = ('title', 'content')
    template_name = 'notes/ideas_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['board'] = Board.objects.get(id=self.kwargs.get('id'))
        context['idea'] = Ideas.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('board', kwargs={'id': self.kwargs.get('id')}))

    def delete(self, request, *args, **kwargs):
        idea_object = Ideas.objects.get(pk=self.kwargs.get('pk'))
        board_object = Board.objects.get(id=self.kwargs.get('id'))

        if board_object.user == self.request.user and idea_object.user == self.request.user:
            messages.error(
                self.request, f"Idea borrada exitosamente")
            return super(IdeaDelete, self).delete(
                request, *args, **kwargs)
        else:
            messages.error(
                self.request, f"No tienes permisos para borrar esta idea")
            return redirect(reverse('ideas-delete', kwargs={'id': self.kwargs.get('id')}))

    def get_success_url(self):
        return reverse('board', kwargs={'id': self.kwargs.get('id')})
