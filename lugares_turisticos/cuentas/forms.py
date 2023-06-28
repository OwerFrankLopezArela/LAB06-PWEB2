from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .models import Cuenta

class RegistroForm(UserCreationForm):
    direccion = forms.CharField(max_length=100)

    class Meta:
        model = Cuenta
        fields = ('username', 'direccion', 'password1', 'password2')

class InicioSesionForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Usuario o contraseña incorrectos')
