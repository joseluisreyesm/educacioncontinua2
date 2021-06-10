from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='eduacionapp'

urlpatterns = [
    path('', views.index, name="index"),
    path('home/', views.Home.as_view(), name='home'),
    path('login/', views.Login.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
]