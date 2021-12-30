from rest_framework import serializers
from .models import TestPayment

class TestPaymentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100)
    amount = serializers.CharField(max_length=10)
    class Meta:
        model = TestPayment
        fields = ['name','amount']