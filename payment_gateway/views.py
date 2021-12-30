from django.http.response import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import razorpay
from rest_framework import status

from .models import TestPayment
from .serializers import TestPaymentSerializer

# Create your views here.
@api_view(['GET'])
def payment_routes(request):
    api_urls = {
        'Register': '/register',
        'Get Tokens': '/token',
        'Refresh Tokens': '/token/refresh'
    }
    return Response(api_urls)

@api_view(['POST'])
def test_payment(request):
    serializer = TestPaymentSerializer(data=request.data)
    if serializer.is_valid():
        name = request.data['name']
        amount = int(request.data['amount'])*100
        client = razorpay.Client(auth = ("rzp_test_11LV9V2xBmW3uJ","qYUSI3HmHEqPjxkXPggT7xlQ"))
        payment = client.order.create({'amount':amount,'currency':'INR','payment_capture':'1'})
        test = TestPayment(name=name,amount=amount,payment_id=payment['id'])
        test.save()
    return Response({'amount':amount,'order_id':payment['id']})

@api_view(['POST'])
def success(request):
    if request.method=='POST':
        order_id = request.data['payload']['payment']['entity']['order_id']
        test = TestPayment.objects.filter(payment_id=order_id).first()
        test.paid = True
        test.save()
    return Response(status=status.HTTP_200_OK)