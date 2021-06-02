from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UsuarioForm(UserCreationForm):
    class Meta:
        model = User

        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'username': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Matrícula'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),

        }

        labels = {
            'username': 'Matrícula',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Correo',
        }

