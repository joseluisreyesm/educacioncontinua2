from django.contrib import auth
from django.shortcuts import render
from .models import Usuario
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import TemplateView
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
from .decorators import unauthenticated_user
from django.utils.decorators import method_decorator


@method_decorator(unauthenticated_user, name='dispatch')
class Register(CreateView):
    model = User
    template_name = "register.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('eduacionapp:login')

# En esta clase se iniciara sesion dentro de la plataforma web
@method_decorator(unauthenticated_user, name='dispatch')
class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('eduacionapp:admin')

class Home (TemplateView):
    template_name = 'Home.html'
    success_url = reverse_lazy('eduacionapp:admin')