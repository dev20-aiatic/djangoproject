from django.http import HttpResponse


# Create your views here.

def helloword(request):
    return HttpResponse('<h2>Hola Mundo:v</h2>')