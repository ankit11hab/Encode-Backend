from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MembersSerializer
from .models import Members

@api_view(['GET'])
def home(request):
    api_urls = {
        'List': '/member-list/',
        'Create': '/member-create/'
    }
    return Response(api_urls)

@api_view(['GET'])
def memberList(request):
    members = Members.objects.all()
    serializer = MembersSerializer(members,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def memberCreate(request):
    serializer = MembersSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
