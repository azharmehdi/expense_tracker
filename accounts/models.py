from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class RegisterUser(AbstractUser):
    first_name = models.CharField(max_length=36)
    middle_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    password =models.CharField()
    username =  models.CharField(unique=True)
    email = models.EmailField(unique=True)
