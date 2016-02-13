# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Professor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Camps del model Usuari per defecte:
    # - is_staff: Té accés al panell d'administració.
    # - username: nom d'usuari
    # - first_name & last_name: nom complert
    # - email: el correu electrònic de l'usuari
    # - 
