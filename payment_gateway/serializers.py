from rest_framework import serializers
from .models import TestPayment

class TestPaymentSerializer(serializers.ModelSerializer):
    amount = serializers.CharField(max_length=10)
    busNumber = serializers.CharField(max_length=100)
    class Meta:
        model = TestPayment
        fields = ['amount','busNumber']

class TestPaymentHistorySerializer(serializers.ModelSerializer):
    payment_id = serializers.CharField(max_length=100)
    amount = serializers.CharField(max_length=10)
    class Meta:
        model = TestPayment
        fields = ['payment_id','amount']