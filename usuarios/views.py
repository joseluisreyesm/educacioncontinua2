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
from django.shortcuts import render, redirect
#importa los grupos que tienen diferentes permisos
from django.contrib.auth.models import Group


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

def Home(request):
    usuarios = User.objects.all()
    context = {'usuarios': usuarios}
    return render(request, 'home.html', context)



class ListaUsuario(ListView):
    model = User

def editar_usuario(request, id):
    usuario = User.objects.get(id=id)
    form = UsuarioForm(instance=usuario)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('eduacionapp:home')
    context = {'form': form}
    return render(request, 'editar_usuario.html', context)

# Elimina un usario
def elimina_usuario(request, id):
    usua = User.objects.get(id=id)
    if request.method == "POST":
        usua.delete()
        return redirect('/')
    context = {'usua': usua}
    return render(request, 'delete.html', context)

#Modifica los permisos de un usuario
def editar_permisos(request, id):
    usua =User.objects.get(id=id)
    group_al = Group.objects.get(name='alumno')
    group_pro = Group.objects.get(name='profesor')


    # seleccionar el tipo de permiso a mano
    if request.method == "POST":
        #identidica el permiso
        #Eres un estudiante
        if '_estudiante' in request.POST:
            print(usua.groups.all()[0])
            #quitamos los grupos
            usua.groups.clear()
            #le da permiso de estudiante
            usua.groups.add(group_al)


        #Entonces eres un profesor
        else:
            # Le da permiso de profesor
            usua.groups.clear()
            usua.groups.add(group_pro)
        #usua.delete()
        return redirect('eduacionapp:home')
    #Se le entrega los datos para mostrarlos
    context = {'usua': usua}
    return render(request, 'editar_permisos.html', context)
