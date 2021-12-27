from django.shortcuts import render
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import MembersSerializer, NotesSerializer
from .models import Members, Notes

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



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def getNotes(request):
    user = request.user
    notes = user.notes_set.all()
    serializer = NotesSerializer(notes,many=True)
    return Response(serializer.data)