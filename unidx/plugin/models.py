from django.db import models

# Create your models here.

class Flux(models.Model):
    pub_datetime = models.DateTimeField('datetime')
    flux = models.DecimalField(default=0.0)