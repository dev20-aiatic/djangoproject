from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('fullname', 'email', 'subject', 'message')
        widgets = {
            'fullname': forms.TextInput(attrs={'class': 'col', 'placeholder': 'Pepito Perez'}),
            'email': forms.EmailInput(attrs={'class': 'col', 'placeholder': 'pepito@msn.com'}),
            'subject': forms.TextInput(attrs={'class': 'col', 'placeholder': 'Urgente...'}),
            'message': forms.Textarea(attrs={'placeholder': 'Tengo una duda respecto...'})
        }

    def form_valid(self, form):
        return super().form_valid(form)



