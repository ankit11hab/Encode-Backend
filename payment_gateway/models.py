from django.db import models
from django.contrib.auth.models import User

from drivers.models import Driver

# Create your models here.
class TestPayment(models.Model):
    passenger = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    bus = models.ForeignKey(Driver,on_delete=models.CASCADE,null=True)
    amount = models.CharField(max_length=10)
    payment_id = models.CharField(max_length=100,default="")
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.payment_id