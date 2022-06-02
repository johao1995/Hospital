from django.contrib.auth import authenticate,login,logout
from django.shortcuts import redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import User
from django.views.generic import (
    TemplateView,
    FormView,
    View
)


class LoginUser(FormView):
    template_name='usuarios/login.html'
    form_class=LoginForm
    success_url=reverse_lazy('usuario:home')

    def dispatch(self,request,*args,**kwargs):
        if request.method=="GET":
            if request.user.is_authenticated:
                return redirect('usuario:home')

        return super().dispatch(request,*args,**kwargs)

    def form_valid(self,form):
        email=form.cleaned_data['email']
        password=form.cleaned_data['password']
        usuario=authenticate(
            email=email,
            password=password
        )
        print(usuario)
        login(self.request,usuario)
        return super().form_valid(form)

class LogoutUser(View):
    def get(self,request):
        logout(self.request)
        return redirect('usuario:login')

class RegisterUser(FormView):
    template_name='usuarios/register.html'
    form_class=RegisterForm
    success_url=reverse_lazy('usuario:login')

    def form_valid(self,form):
        email=form.cleaned_data['email']
        password1=form.cleaned_data['password1']
        User.objects.create_user(
            email,
            password1,
            first_name=form.cleaned_data['first_name'],
            last_name=form.cleaned_data['last_name'],
            genero=form.cleaned_data['genero']
        )
        return super().form_valid(form)

class HomePage(LoginRequiredMixin,TemplateView):
    template_name='home.html'
    login_url=reverse_lazy('usuario:login')