from .forms import RegisterForm
from .models import Pacientes
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
    View
)

class ListPaciente(ListView):
    template_name='paciente/lista_paciente.html'
    context_object_name='paciente'

    def get_queryset(self):
        txt_dato=self.request.GET.get('txt_dato','')

        paciente=Pacientes.objects.lista_pacientes(txt_dato)
        return paciente

class CreatePaciente(CreateView):
    model=Pacientes
    template_name='paciente/register.html'
    form_class=RegisterForm
    success_url=reverse_lazy('paciente:list-paciente')

class DeletePaciente(DeleteView):
    template_name='paciente/delete_paciente.html'
    context_object_name='paciente'
    model=Pacientes
    success_url=reverse_lazy('paciente:list-paciente')

class UpdatePaciente(UpdateView):
    template_name='paciente/update_paciente.html'
    form_class=RegisterForm
    model=Pacientes
    success_url=reverse_lazy('paciente:list-paciente')


class ListFecha(ListView):
    template_name='paciente/lista_paciente.html'
    context_object_name='paciente'

    def get_queryset(self):
        fecha_inicial=self.request.GET.get('fecha_inicial')
        fecha_final=self.request.GET.get('fecha_final')
        print(fecha_inicial)
        paciente=Pacientes.objects.lista_fecha_pacientes(fecha_inicial,fecha_final)
        return paciente