from django.contrib import admin
from . models import Cliente, Habitacion, Pais, TipoHab

# Register your models here.

admin.site.register(Cliente)
admin.site.register(Habitacion)
admin.site.register(Pais)
admin.site.register(TipoHab)