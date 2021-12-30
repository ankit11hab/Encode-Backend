from django.db import models

# Create your models here.
class TestPayment(models.Model):
    name = models.CharField(max_length=100)
    amount = models.CharField(max_length=10)
    payment_id = models.CharField(max_length=100)
    paid = models.BooleanField(default=False)