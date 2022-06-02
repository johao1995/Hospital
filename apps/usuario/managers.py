from django.db import models
from django.contrib.auth.models import BaseUserManager

class UserManager(BaseUserManager,models.Manager):
    def __create_user(self,email,password,is_staff,is_superuser,**extra_fields):
        user=self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user
    
    def create_user(self,email,password,**extra_fields):
        return self.__create_user(email,password,False,False,**extra_fields)
        
    def create_superuser(self,email,password,**extra_fields):
        return self.__create_user(email,password,True,True,**extra_fields)