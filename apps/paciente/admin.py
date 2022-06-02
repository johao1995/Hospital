from django.contrib import admin
from .models import Pacientes

class PacienteAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'first_name',
        'last_name',
        'dni',
        'genero',
        'fecha_atencion'
    )

admin.site.register(Pacientes,PacienteAdmin)