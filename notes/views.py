from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from requests import Response

from .forms import NewBoard
from .models import Ideas, Board


# Board's Views

class BoardList(ListView):
    model = Board
    template_name = 'notes/board_list.html'
    context_object_name = 'board'
    ordering = ['-updated_at']
    paginate_by = 8


class BoardCreate(CreateView):
    model = Board
    template_name = 'notes/board_create.html'
    fields = ['name', 'user', 'public']

    def get_success_url(self):
        return reverse('boards')

    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(*args, **kwargs)
        initial['user'] = self.request.user
        return initial

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, f"Tablero creado correctamente!")
        form.save()
        return super().form_valid(form)


class BoardUpdate(UpdateView):
    model = Board
    template_name = 'notes/board_update.html'
    fields = '__all__'
    context_object_name = 'board'


class BoardDelete(DeleteView):
    model = Board
    context_object_name = 'board'
    template_name = 'notes/board_list.html'
    success_url = reverse_lazy('boards')

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')


        # Ideas' Views

class IdeaList(ListView):
    model = Ideas
    context_object_name = 'ideas'


class IdeaDetail(DetailView):
    model = Ideas
    context_object_name = 'ideas'
    template_name = 'notes/ideas.html'


class IdeaCreate(CreateView):
    model = Ideas
    fields = ['title', 'content']
    context_object_name = 'ideas'


class IdeaUpdate(UpdateView):
    model = Ideas
    context_object_name = 'ideas'


class IdeaDelete(DeleteView):
    model = Board
    context_object_name = 'ideas'
    success_url = reverse_lazy('boards')
