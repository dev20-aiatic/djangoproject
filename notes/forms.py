from django import forms
from .models import Board


class NewBoard(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('name', 'user', 'public')

        widgets = {
            'user': forms.HiddenInput(),
        }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
