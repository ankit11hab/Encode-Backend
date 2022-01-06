from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import server_error

from .models import Profile

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=80, min_length=5, write_only=True)
    password2 = serializers.CharField(max_length=80, min_length=5, write_only=True)
    email = serializers.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password','password2']

    def validate(self, attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError({'password':('Passwords do not match!')})
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email':('Email is already in use!')})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)

class ProfileSerializer(serializers.ModelSerializer):
    first_name=serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    phone=serializers.CharField(max_length=100)
    isDriver = serializers.BooleanField()
    class Meta:
        model = Profile
        fields = ['first_name','last_name','phone','isDriver']