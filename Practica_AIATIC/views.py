from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView

from Practica_AIATIC.forms import RegistrationForm
from .models import User


def helloword(request):
    return HttpResponse('<h2>Hola Mundo:v</h2>')


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def profile(request):
    return render(request, 'profile.html', context={"user": request.user})


def debug(request):
    return render(request, 'login.html')


class RegistrationView(CreateView):
    # Signup View extended

    # change template's name and path
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


class ProfileView(UpdateView):
    model = User
    fields = ['email', 'username', 'first_name', 'last_name', 'id_num', 'profile_picture', 'last_login']
    template_name = 'account/profile.html'

    def get_success_url(self):
        return reverse('home')

    def get_object(self, **kwargs):
        return self.request.user
