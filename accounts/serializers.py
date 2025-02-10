from rest_framework import serializers
from .models import RegisterUser


class UserRegister(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ['first_name','middle_name','last_name','email','password','username']

    