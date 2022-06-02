from django.urls import path
from . import views

usuario_urlpatterns=([
    path('',views.LoginUser.as_view(),name='login'),
    path('logout/',views.LogoutUser.as_view(),name='logout'),
    path('register-user/',views.RegisterUser.as_view(),name='register-user'),
    path('home/',views.HomePage.as_view(),name='home')
],'usuario')