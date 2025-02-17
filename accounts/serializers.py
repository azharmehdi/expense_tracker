from rest_framework import serializers
from .models import RegisterUser as RegisterUser


class UserRegister(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = RegisterUser
        fields = ['first_name','middle_name','last_name','email','password','username']

    def validate_first_name(self,value):
        if not value.isalpha():
            raise serializers.ValidationError ("First name must contain only letters")
        return value
        
    def validate_middle_name(self, value):
        if value and not value.isalpha():
            raise serializers.ValidationError("Middle name must contain only letters")
        return value
    
    def validate_last_name(self,value):
        if not value.isalpha():
            raise serializers.ValidationError('Last name must contain only letters')
        return value
    
    def validate_password(self, value):
        if len(value) <= 7:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        return value
    
    def create(self, validated_data):
        return RegisterUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            middle_name=validated_data.get('middle_name', ''),
            last_name=validated_data['last_name']
        )