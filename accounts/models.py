from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class RegisterUser(AbstractUser):
    first_name = models.CharField(max_length=36)
    middle_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    password = models.CharField(max_length=128)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
