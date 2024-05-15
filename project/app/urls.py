from django.urls import path
from .views import *

urlpatterns=[
    path('',home,name='home'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
    path('register/',register,name='register'),
    path('registerdata/',registerdata,name='registerdata'),
    path('login/',login,name='login'),
    path('logindata/',logindata,name='logindata'),
    path('dashboard/',dashboard,name='dashboard'),
    # path('',dashboard,name='dashboard'),

]