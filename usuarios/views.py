from django.contrib import auth
from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.contrib.auth import logout


def index(request):
    plantilla = 'usuarios/index.html'
    return render(request, plantilla)

###### Usuarios general
class NuevoUsuario(CreateView):
    model = User
    template_name = "signup.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('eduacionapp:login')

class UsuarioActualizar(UpdateView):
    #model = Usuario
    fields = '__all__'
    extra_context = {'etiqueta': 'Actualizar', 'boton': 'Guardar'}
    #success_url = reverse_lazy('escolarapp:perfil')

class SignupUsuario(LoginView):
    #model = Usuario
    template_name = 'usuarios/signup.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('escolarapp:login')

#### Usuario administrador

class UsuarioEliminar(DeleteView):
    #model = Usuario
    success_url = reverse_lazy('escolarapp:lista')

class LoginUsuario(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('eduacionapp:admin')

@login_required
def prueba(request):
        return HttpResponse("Hola quiero dormir")

def pruebaus(request):
    plantilla = 'eduacionapp/pruebaus.html'
    return render(request, plantilla)
@login_required
def usuarioAlumno(request):
    plantilla = 'usuarios/alumnos.html'
    return render(request, plantilla)
@login_required
def usuarioProfesor(request):
    plantilla = 'usuarios/profesores.html'
    return render(request, plantilla)
