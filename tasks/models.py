from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' -by ' + self.user.username


class Propietario(models.Model):
    nombresCompletos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    telefonoAuxiliar = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class FamiliarDifunto(models.Model):
    nombresCompletos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    telefonoAuxiliar = models.CharField(max_length=100, blank=True)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Boveda(models.Model):
    ubicacion = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    idPropietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)


class Difunto(models.Model):
    nombresCompletos = models.CharField(max_length=100)
    fechaNacimiento = models.DateTimeField()
    fechaDefuncion = models.DateTimeField()
    fechaDejoEnBoveda = models.DateTimeField()
    fechaFinAlquiler = models.DateTimeField(null=True, blank=True)
    idBoveda = models.ForeignKey(Boveda, on_delete=models.CASCADE)
    idFamiliar = models.ForeignKey(FamiliarDifunto, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
