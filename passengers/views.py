from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from payment_gateway.models import TestPayment
from rest_framework.permissions import IsAuthenticated
import json

# Create your views here.
@api_view(['GET'])
def passenger_routes(request):
    return Response("ok")


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def passenger_history(request):
    user = request.user
    history = TestPayment.objects.filter(passenger=user,paid=True)
    toBeReturned = []
    for item in history:
        obj = {
            "amount":item.amount,
            "paymentID": item.payment_id,
            "busNumber": item.bus.busNumber
        }
        toBeReturned.append(obj)
    
    return Response(json.dumps(toBeReturned))