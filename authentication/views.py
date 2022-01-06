from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.utils import serializer_helpers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
import uuid
from rest_framework.permissions import IsAuthenticated

from .models import Profile
from .serializers import ProfileSerializer, UserSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        profile = Profile.objects.filter(user=user).first()
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['first_name'] = profile.first_name
        token['last_name'] = profile.last_name
        token['phone'] = profile.phone
        token['isDriver'] = profile.isDriver
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def routes(request):
    api_urls = {
        'Register': '/register',
        'Get Tokens': '/token',
        'Refresh Tokens': '/token/refresh'
    }
    return Response(api_urls)

class RegisterView(GenericAPIView):
    serializer_class = UserSerializer
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user=User.objects.filter(username=request.data['username']).first()
            auth_token = str(uuid.uuid4())
            print(user,auth_token)
            Profile(user=user,auth_token=auth_token).save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def profile(request):
    print(request.data['first_name'])
    profile = Profile.objects.filter(user=request.user).first()
    profile.first_name = request.data['first_name']
    profile.last_name = request.data['last_name']
    profile.phone = request.data['phone']
    profile.isDriver = request.data['is_driver']
    profile.save()
    return Response(status=status.HTTP_200_OK)