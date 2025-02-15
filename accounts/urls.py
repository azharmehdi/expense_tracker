from django.conf import urls
from django.urls import path
from .views import *

urlsPatterens = [
    path('/register',register,name='register'),
    path('/login',login,name='login')
]