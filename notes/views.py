from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Ideas, Board


# Board's Views

class BoardList(ListView):
    model = Board
    template_name = 'notes/board_list.html'
    context_object_name = 'board'


class BoardCreate(CreateView):
    model = Board
    template_name = 'notes/board_create.html'
    fields = ['name', 'public', 'private']
    context_object_name = 'board'

    def get_success_url(self):
        return reverse('boards')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class BoardUpdate(UpdateView):
    model = Board
    template_name = 'notes/board_update.html'
    context_object_name = 'board'


class BoardDelete(DeleteView):
    model = Board
    template_name = 'notes/board_update.html'
    context_object_name = 'board'
    success_url = reverse_lazy('boards')
    pk_url_kwarg = 'custom_pk'


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
