from django.db import models
from .choices import estados
from django.contrib.auth.models import User

# Create your models here.

class Residencia(models.Model):
    nro = models.IntegerField(primary_key = True)
    dueño = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    mail = models.EmailField()

    def __str__(self):
        return str(self.nro)


class Correspondencia(models.Model):
    conserje = models.ForeignKey(User, limit_choices_to={'groups__name':"conserje"}, on_delete=models.CASCADE)
    remitente = models.CharField(max_length=30)
    destinatario = models.CharField(max_length=30)
    estado = models.CharField(max_length=1, choices=estados, default='P')
    fechaRecepcion = models.DateField()
    nroResidencia = models.ForeignKey(Residencia, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.nroResidencia)
