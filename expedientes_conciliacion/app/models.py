from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    clave_empleado = models.CharField(max_length=20, unique=True)
    puesto = models.IntegerField()  # 1: Administrador, 2: Usuario normal

    def __str__(self):
        return self.nombre

    def es_administrador(self):
        return self.puesto == 1