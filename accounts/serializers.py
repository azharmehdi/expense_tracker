from rest_framework import serializers
from .models import RegisterUser as User


class UserRegister(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name','middle_name','last_name','email','password','username']

    def validate_first_name(self,value):
        if not value.isalpha():
            raise serializers.ValidationError ("First name must contain only letters")
        return value
        
    def validate_middle_name(self,value):
        if not value.isalpha():
            raise serializers.ValidationError('Middle name must contain only letters')
        return value
    
    def validate_last_name(self,value):
        if not value.isalpha():
            raise serializers.ValidationError('Last name must contain only letters')
        return value
    
    def validate_password(self,value):
        if value.len() <=7:
            raise serializers.ValidationError('Password must be at least 8 characters long')
        return value
    
    def create(self,validated_data):
        user =User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user