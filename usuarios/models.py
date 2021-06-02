from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as gettext


# Create your models here.

class Usuario(models.Model):
    matricula = models.IntegerField()
