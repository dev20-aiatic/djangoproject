from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView

from website.forms import ContactForm


class Index(TemplateView):
    template_name = 'website/home.html'
    context_object_name = 'websites'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class About(TemplateView):
    template_name = 'website/about.html'
    context_object_name = 'websites'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Services(TemplateView):
    template_name = 'website/services.html'
    context_object_name = 'websites'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class Contact(FormView):
    template_name = 'website/contact.html'
    form_class = ContactForm
    success_url = '/contacto/'

    def form_valid(self, form):
        messages.success(self.request, 'Su mensaje ha sido enviado')
        return super(Contact, self).form_valid(form)


class Received(TemplateView):
    model = Contact
    template_name = 'website/received.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        bar = self.request.POST.get('email', None)
        context['received'] = 'new_variable' + ' updated'
        return self.render_to_response(context)
