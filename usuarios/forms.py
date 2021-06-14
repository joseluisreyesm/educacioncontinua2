from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms

#Este es el form del registro del usuario en la plataforma
class UsuarioForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'Introduce tu contraseña'
        self.fields['password2'].label = 'Introduce tu contraseña nuevamente'
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'username': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Matrícula'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electrónico'}),
        }