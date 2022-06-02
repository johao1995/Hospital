from django.db import models
from .managers import PacienteQuerys

class Pacientes(models.Model):
    genero_choices=(
        ('M','Masculino'),
        ('F','Femenino')
    )
    first_name=models.CharField(max_length=30,verbose_name='Nombre')
    last_name=models.CharField(max_length=30,verbose_name='Apellido')
    dni=models.IntegerField(verbose_name='Dni')
    genero=models.CharField(max_length=1,choices=genero_choices,verbose_name='Genero')
    fecha_atencion=models.DateField(verbose_name='Fecha Atencion')
    objects=PacienteQuerys()
    
    class Meta:
        verbose_name_plural='paciente'
        db_table='paciente'
        ordering=('id',)

    def __str__(self):
        return self.first_name
    
