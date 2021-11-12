from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from .models import Profile


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ['email', 'username', 'first_name', 'last_name', 'id_num', 'profile_picture', 'password']

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Profile
        fields = ['email', 'username', 'first_name', 'last_name', 'id_num', 'profile_picture', 'password']


# Admin Panel Form

class UsersCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Profile
        fields = ('email', 'username', 'first_name', 'last_name', 'id_num',
                  'profile_picture', 'password', 'is_staff', 'is_admin')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("Contraseña")
        password2 = self.cleaned_data.get("Verificación de contraseña")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Las contraseñas no son iguales")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UsersChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Profile
        fields = ['email', 'username', 'first_name', 'last_name', 'id_num',
                  'profile_picture', 'password', 'is_active', 'is_admin']

    def clean_password(self):
        return self.initial["password"]
