from django.db import models

# Create your models here.
class Actividades(models.Model):
    nombreTarea = models.CharField(max_length=100)
    tiempoTarea = models.IntegerField()
    tiempofinal = models.IntegerField()
    fechaTarea = models.DateField()