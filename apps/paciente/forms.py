from django import forms
from .models import Pacientes

class RegisterForm(forms.ModelForm):
    class Meta:
        model=Pacientes
        fields=(
            'first_name',
            'last_name',
            'dni',
            'genero',
            'fecha_atencion'
        )
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'last_name'}),
            'dni':forms.TextInput(attrs={'class':'form-control','placeholder':'Dni'}),
            'genero':forms.Select(attrs={'class':'form-control','placeholder':'Genero'}),
            'fecha_atencion':forms.DateInput(attrs={'class':'form-control','type':'date'})
            
        }
