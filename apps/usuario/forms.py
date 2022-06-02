from django import forms
from .models import User
from django.contrib.auth import authenticate

class LoginForm(forms.Form):
    email=forms.EmailField(max_length=30,widget=forms.EmailInput(
        attrs={
            'class':'form-control',
            'placeholder':'email'
        }
    ))
    password=forms.CharField(max_length=30,widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'password'
        }
    ))

    def clean(self):
        email=self.cleaned_data['email']
        password=self.cleaned_data['password']
        user=authenticate(email=email,password=password)
        if user is None:
            print(User)
            raise forms.ValidationError("Usuario Incorrecto")
        

class RegisterForm(forms.ModelForm):
    password1=forms.CharField(max_length=20,widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'password'
        }
    ))
    password2=forms.CharField(max_length=20,widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'comfirm password'
        }
    ))
    class Meta:
        model=User
        fields=(
            'email',
            'first_name',
            'last_name',
            'genero',
        )
        widgets={
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'ejemplo@gmail.com'}),
            'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'first_name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'last_name'}),
            'genero':forms.Select(attrs={'class':'form-control','placeholder':'genero'})
        }
    def clean_password2(self):
        password1=self.cleaned_data['password1']
        password2=self.cleaned_data['password2']

        if password1!=password2:
            raise forms.ValidationError("Los password no coinciden")