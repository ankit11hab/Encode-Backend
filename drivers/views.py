from django.db.models.fields import json
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from drivers.models import Driver

# Create your views here.
@api_view(['GET'])
def driver_routes(request):
    return Response("ok")

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def driver_details(request):
    user = request.user
    if request.data['busNumber']:
        Driver(driver=user,busNumber= request.data['busNumber']).save()
        return Response("Driver updated successfully")
    return Response("Enter valid details")


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def bus_route(request):
    user = request.user
    route = request.data['route']
    driver = Driver.objects.filter(driver=user).first()
    driver.route = route
    driver.save()
    return Response("Bus Route updated successfully")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_driver_details(request):
    user = request.user
    driver = Driver.objects.filter(driver=user).first()
    busNumber = driver.busNumber
    totalRevenue = driver.totalRevenue
    api = {
        "busNumber":busNumber,
        "totalRevenue":totalRevenue,
    }
    return Response(api)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_bus_route(request):
    user = request.user
    driver = Driver.objects.filter(driver=user).first()
    route = (driver.route)
    return Response(route)