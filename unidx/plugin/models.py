from django.db import models

#### TABLA DEL HISTORIAL DE LAS BUSQUEDAS AQUI

class Visitante(models.Model):
    nombre = models.CharField(max_length=150)
    
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
