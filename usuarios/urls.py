from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='eduacionapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('login/', views.LoginUsuario.as_view(), name='login'),
    path('register/', views.NuevoUsuario.as_view(), name='register'),
    path('actualizar/<int:pk>', views.UsuarioActualizar.as_view(), name='actualizar'),
    path('prueba/', views.prueba, name='prueba'),
    path(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('alumno/', views.usuarioAlumno, name='alumno'),
    path('profesor/', views.usuarioProfesor, name='profesor'),
]