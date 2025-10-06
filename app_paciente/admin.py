from django.contrib import admin

# Register your models here.

from .models import Paciente
# Registrar el modelo Paciente en el Admin
admin.site.register(Paciente)