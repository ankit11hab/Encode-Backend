from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Driver(models.Model):
    driver = models.OneToOneField(User,on_delete=models.CASCADE)
    busNumber = models.CharField(max_length = 100,default="")
    route = models.CharField(max_length=100000,default="")
    totalRevenue = models.IntegerField(default=0)

    def __str__(self):
        return f'driver'
