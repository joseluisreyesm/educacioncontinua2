from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .decorators import unauthenticated_user
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.shortcuts import render


#Esta clase se utiliza para realizar el registro de un nuevo usuario en la plataforma web
@method_decorator(unauthenticated_user, name='dispatch')
class Register(CreateView):
    model = User
    template_name = "register.html"
    form_class = UsuarioForm
    success_url = reverse_lazy('eduacionapp:login')

#Esta clase se utiliza para iniciar sesion dentro de la plataforma web
@method_decorator(unauthenticated_user, name='dispatch')
class Login(LoginView):
    template_name = 'login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('eduacionapp:admin')

#Esta clase es para organizar el contenido base de la plataforma web
class Home (TemplateView):
    template_name = 'Home.html'
    success_url = reverse_lazy('eduacionapp:admin')
    usuarios = User.objects.all()
    extra_context = ({'usuarios': usuarios})
    def lista(request):
        usuarios = User.objects.all()
        return render(request, 'home.html', {'usuarios': usuarios})

class ListaUsuario(ListView):
    model = User
