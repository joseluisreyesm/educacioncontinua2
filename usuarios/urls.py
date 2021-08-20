from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from . import templates

app_name='eduacionapp'

#Aqui se determinan las urls a las que se puede acceder a la página
urlpatterns = [
    path('home/', views.Home, name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('editar/<int:id>', views.editar_usuario, name='editar'),
    path('editar_permisos/<int:id>', views.editar_permisos, name='editar_permisos'),
    path('delete/<int:id>/', views.elimina_usuario, name='borrar'),
    path(r'logout/', auth_views.LogoutView.as_view(), name='logout'),


]