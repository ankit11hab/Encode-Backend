from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TestPayment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    amount = models.CharField(max_length=10)
    payment_id = models.CharField(max_length=100,default="")
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.payment_id