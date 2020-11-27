from django.db import models
from django.urls import reverse
import uuid

# Create your models here.

class Pais(models.Model):
    id_pais = models.IntegerField(primary_key=True)
    nombre_pais = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre_pais


class TipoHab(models.Model):
    id_tipo = models.IntegerField(primary_key=True)
    nombre_habitacion = models.CharField(max_length=50)
    beneficios = models.CharField(max_length=300)
    
    def __str__(self):
        return self.nombre_habitacion
    

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=15)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    pais = models.ForeignKey('Pais', on_delete=models.SET_NULL, null = True)
    edad = models.IntegerField(help_text='Escriba solo los años')
    email = models.EmailField(max_length=200)
    direccion = models.CharField(max_length=200)
    password = models.CharField(max_length=20, help_text='El largo debe ser entre 8 y 20 caracteres')
    
    def __str__(self):
        return f'{self.nombres} ({self.apellidos})'
    
    def get_absolute_url(self):
        return reverse('cliente-detail',args=[str(self.rut)])
    

class Habitacion(models.Model):
    id_habitacion = models.IntegerField(primary_key=True)
    id_tipo = models.ForeignKey('TipoHab', on_delete=models.SET_NULL, null=True)
    caracteristicas = models.TextField(help_text='Defina todas las características de la habitación')
    descripcion = models.TextField(help_text='Descripción de la habitación')
    servicios = models.TextField(help_text='Defina los servicios de la habitación')
    equipamiento = models.TextField(help_text='Defina el equipamiento de la habitación')
    image_1= models.ImageField(upload_to='images/', null=True, blank=True)
    image_2= models.ImageField(upload_to='images/', null=True, blank=True)
    
    def __str__(self):
        return str(self.id_habitacion)
    
    def get_absolute_url(self):
        return reverse('habitacion-detail',args=[str(self.id_habitacion)])
