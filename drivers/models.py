from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Driver(models.Model):
    driver = models.OneToOneField(User,on_delete=models.CASCADE)
    busNumber = models.CharField(max_length = 100,default="")
    totalRevenue = models.IntegerField(default=0)

    def __str__(self):
        return self.driver.username



class BusRoute(models.Model):
    bus = models.ForeignKey(Driver,on_delete=models.CASCADE)
    place_id = models.CharField(max_length=100,default="")
    place_name = models.CharField(max_length=100,default="")
    expected_time = models.TimeField(null=True)

    def __str__(self):
        return self.bus.driver.username