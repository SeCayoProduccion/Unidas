from django.db import models
#indraa
# tabla para guardar que busco cada visitante, no guarda su nombre por privacidad
class Visitante(models.Model):
    sexo = models.CharField(max_length=20)
    edad = models.CharField(max_length=10, blank=True)
    estado = models.CharField(max_length=100)
    
    fecha = models.DateField(auto_now_add=True) # Se guarda solita cuando crea el registro
    hora = models.TimeField(auto_now_add=True) # lo mismo que con fecha

    def __str__(self):
        return f"{self.estado} - {self.sexo} - {self.fecha}"
