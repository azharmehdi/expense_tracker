from django.db import models

# Create your models here.

class RegisterUser(models.Model):
    first_name = models.CharField(max_length=36)
    middle_name = models.CharField(max_length=36)
    last_name = models.CharField(max_length=36)
    password =models.CharField()
    username =  models.CharField(unique=True)
    e_mail = models.EmailField(unique=True)
