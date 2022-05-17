from django.contrib import admin
from .models import Modelo, Marca, Carro

admin.site.register(Modelo)
admin.site.register(Carro)
admin.site.register(Marca)

# Register your models here.
