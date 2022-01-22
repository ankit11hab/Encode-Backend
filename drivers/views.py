from datetime import datetime
from django.db.models.fields import json
from django.http.response import JsonResponse
from django.shortcuts import render
from phonenumbers import expected_cost
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import BusRoute
from payment_gateway.models import TestPayment
import datetime
import uuid
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

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_bus_route(request):
    user = request.user
    place_name = request.data['place_name']
    place_id = request.data['place_id']
    expected_time = request.data['expected_time']
    driver = Driver.objects.filter(driver=user).first()
    BusRoute(bus=driver,place_name=place_name,expected_time=expected_time,place_id = place_id).save()
    return Response("OK")


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def get_buses(request):
    place_id = request.data['place_id']
    bus = BusRoute.objects.filter(place_id=place_id)
    toBeList = []
    for busRoute in bus:
        obj = {"busNumber":busRoute.bus.busNumber,"expected_time": busRoute.expected_time}
        toBeList.append(obj)
    resp = {
        "data":toBeList
    }
    return Response(resp)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def get_bus_description(request):
    busNumber = request.data['busNumber']
    bus = Driver.objects.filter(busNumber=busNumber).first()
    routes = bus.busroute_set.all()
    toBeReturned = []
    for route in routes:
        obj = {"location":route.place_name,"expected_time": route.expected_time}
        toBeReturned.append(obj)
    resp = {
        "data":toBeReturned
    }
    return Response(resp)


@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def book_ticket(request):
    user = request.user
    busNumber = request.data['busNumber']
    bus = Driver.objects.filter(busNumber=busNumber).first()
    TestPayment(passenger=user,bus=bus,date=datetime.datetime.now(),amount=10,payment_id=str(uuid.uuid4()),paid=True).save()
    return Response("OK")