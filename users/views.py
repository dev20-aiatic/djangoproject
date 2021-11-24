from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from users.forms import RegistrationForm, ProfileUpdateForm
from users.models import Profile
from users.serializers import ProfileSerializer

User = get_user_model()


# Create your views here.

@login_required
def home(request):
    return render(request, 'dashboard.html')


# RestFramework Views

class RestUsersList(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_object(self):
        return get_object_or_404(User, id=self.request.query_params.get("id"))

    def get_queryset(self):
        return User.objects.all()


# Custom Auth Views

class RegistrationView(CreateView):
    template_name = 'account/signup.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(**kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        success_url = reverse('login')
        if next_url:
            success_url += '?next={}'.format(next_url)

        return success_url


# Profile Frontend Views

class ProfileDetail(DetailView):
    template_name = 'account/profile.html'
    queryset = User.objects.all()

    def get_object(self, **kwargs):
        id_ = self.kwargs.get("username")
        user = get_object_or_404(User, username=id_)
        return user

    def get_success_url(self):
        return reverse('profile', kwargs={"username": self.request.user.username})

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileDetail, self).get_context_data(**kwargs)
        # user_id = self.kwargs.get('id')
        # user = get_object_or_404(User,id=user_id)
        return context


class ProfileEdit(UpdateView):
    model = Profile
    template_name = 'account/profile_edit.html'
    form_class = ProfileUpdateForm

    def get_object(self, **kwargs):
        return self.request.user

    def get_success_url(self):
        return reverse('profile', kwargs={"username": self.request.user.username})

    def form_valid(self, form):
        messages.success(self.request, f"¡Perfil modificado correctamente!")
        return super().form_valid(form)
