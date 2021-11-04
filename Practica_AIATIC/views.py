from django.http import HttpResponse


# Create your views here.
from django.shortcuts import render


def helloword(request):
    return HttpResponse('<h2>Hola Mundo:v</h2>')

def login(request):
    return render(request, 'login.html')