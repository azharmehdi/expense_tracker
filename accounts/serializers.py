from rest_framework import serializers
from .models import RegisterUser


class UserRegister(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ['first_name','middle_name','last_name','email','password','username']

    def validate_first_name(self,value):
        if not value.isalpha():
            raise serializers.ValidationError ("First name must contain only letters")
        return value
        
    def validate_middle_name(self,value):
        if not value.isalpha():
            raise serializers.ValidationError('Middle name must contain only letters')
        return value
    
    