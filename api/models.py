from django.db import models

class Perros (models.Model):
    NombreMascota=models.CharField(max_length=20)
    Raza=models.CharField(max_length=10)

    def __str__(self):
        return self.NombreMascota
