from django.db import models

class PacienteQuerys(models.Manager):
    def lista_pacientes(self,txt_dato):
        paciente=self.filter(first_name__contains=txt_dato)
        return paciente
    
    def lista_fecha_pacientes(self,fecha_inicial,fecha_final):
        paciente=self.filter(fecha_atencion__range=(fecha_inicial,fecha_final))
        return paciente