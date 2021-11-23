from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('fullname','email', 'subject', 'message')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)