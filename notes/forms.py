from django import forms
from .models import Board, Ideas


class NewBoard(forms.ModelForm):
    class Meta:
        model = Board
        fields = ('name', 'user', 'status')

        widgets = {
            'user': forms.HiddenInput(),
        }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class NewIdea(forms.ModelForm):
    class Meta:
        model = Ideas
        fields = ('title', 'content', 'user', 'board')

        widgets = {
            'user': forms.HiddenInput(),
            'board': forms.HiddenInput(),
        }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)