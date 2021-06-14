from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    matricula = models.IntegerField()
