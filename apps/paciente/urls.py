from django.urls import path
from . import views

paciente_urlpatterns=([
    path('register-paciente/',views.CreatePaciente.as_view(),name='register-paciente'),
    path('list-paciente/',views.ListPaciente.as_view(),name='list-paciente'),
    path('update-paciente/<pk>',views.UpdatePaciente.as_view(),name='update-paciente'),
    path('delete-paciente/<pk>',views.DeletePaciente.as_view(),name='delete-paciente'),
    path('list-fecha_paciente/',views.ListFecha.as_view(),name='list-fecha_paciente')
],'paciente')