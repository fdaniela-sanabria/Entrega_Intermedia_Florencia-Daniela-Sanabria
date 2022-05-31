from concurrent.futures.process import _MAX_WINDOWS_WORKERS
from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

class Profesion(models.Model):
    profesion = models.CharField(max_length=100)

class Vinculo(models.Model):
    vinculo = models.CharField(max_length=100)
