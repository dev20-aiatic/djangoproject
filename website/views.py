from django.contrib import messages
from django.http import Http404
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, FormView, DeleteView, DetailView, UpdateView
from rest_framework import permissions

from website.forms import ContactForm
from website.models import Contact, Feedback


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


class ContactCreate(FormView):
    model = Contact
    template_name = 'website/contact.html'
    form_class = ContactForm
    success_url = '/contacto/'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, f"¡Gracias por contactarse con nosotros!")
        return super().form_valid(form)


class ContactDetail(DetailView):
    model = Contact
    context_object_name = 'contact'
    template_name = 'website/contact_detail.html'

    def get_object(self, queryset=None):
        return Contact.objects.get(pk=self.kwargs.get("pk"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ContactUpdate(UpdateView):
    model = Contact
    template_name = 'website/contact_update.html'
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return reverse('inbox')

    def form_valid(self, form):
        messages.success(self.request, f"Mensaje modificado exitosamente")
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse('message-update', kwargs={'pk': self.kwargs.get('pk')})


class ContactDelete(DeleteView):
    model = Contact
    form_class = ContactForm
    template_name = 'website/contact_delete.html'
    success_url = reverse_lazy('inbox')
    permission_classes = [permissions.IsAuthenticated]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact'] = Contact.objects.get(pk=self.kwargs.get('pk'))
        return context

    def get(self, request, *args, **kwargs):
        try:
            return super().get(request, *args, **kwargs)
        except Http404:
            return redirect(reverse('inbox'))

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, f"¡Mensaje eliminado exitosamente!")
        return super(ContactDelete, self).delete(request, *args, **kwargs)


class ReceivedView(TemplateView):
    model = Feedback
    template_name = 'website/received.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['msg'] = Contact.objects.all()
        return context

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        bar = self.request.POST.get('email', None)
        context['msg'] = 'new_variable' + ' updated'
        return self.render_to_response(context)
