from django.db import models

class Cliente(models.Model):

    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    vehiculo = models.CharField(max_length=50)
    placa = models.CharField(max_length=20)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre