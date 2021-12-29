from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import server_error

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=80, min_length=5, write_only=True)
    password2 = serializers.CharField(max_length=80, min_length=5, write_only=True)
    email = serializers.EmailField()
    first_name = serializers.CharField(max_length=80, min_length=2)
    last_name = serializers.CharField(max_length=80, min_length=2)

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','password2']

    def validate(self, attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError({'password':('Passwords do not match!')})
        if User.objects.filter(email=attrs['email']).exists():
            raise serializers.ValidationError({'email':('Email is already in use!')})
        return super().validate(attrs)

    def create(self, validated_data):
        validated_data.pop('password2')
        return User.objects.create_user(**validated_data)