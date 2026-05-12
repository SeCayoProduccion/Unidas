from django.db import models
import uuid

class Flux(models.Model):
    date_time = models.DateTimeField("date_time", primary_key=True)
    flux = models.FloatField(default=0.0)
    name = models.CharField(max_length=128, default="")

# Create your models here.
# Ok ahora a continuacion aqui estamos creando columnas para buscar en la base de datos.... el csv
# Estas columas son las del nombre, edad de la persona, la entidad (el estado donde viven) y su genero... guardara el input del usuario que escribio

class MyUser(models.Model):
    
    # Opciones para la columna de género que mencionas en tu nota
    GENERO_CHOICES = [
        ('MUJER', 'Mujer'),
        ('HOMBRE', 'Hombre'),
        ('OTRO', 'Otro'),
    ]
# aqui estamos creando las columnas para guardar la informacion que el usuario escriba
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=128, default="")
    edad = models.IntegerField(default=18) #Integer para que solo puedan escribir numeros
    entidad = models.CharField(max_length=128, default="CIUDAD DE MEXICO")
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES, default='MUJER')

    def __str__(self):
        return self.nombre
