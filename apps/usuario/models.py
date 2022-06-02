from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    genero_choices=(
        ('H','Masculino'),
        ('F','Femenino')
    )
    email=models.EmailField(unique=True,blank=False,verbose_name='Email')
    first_name=models.CharField(max_length=30,verbose_name='Nombre')
    last_name=models.CharField(max_length=30,verbose_name='Apelllidos')
    genero=models.CharField(max_length=1,choices=genero_choices,verbose_name='Genero')
    is_staff=models.BooleanField(default=False,verbose_name='Estado')

    objects=UserManager()
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=('genero',)

    class Meta:
        verbose_name_plural='Usuario'
        db_table='usuario'

    def __str__(self):
        return self.first_name
    

