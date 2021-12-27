from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Members(models.Model):
    name = models.CharField(max_length=100,default="")
    module = models.CharField(max_length=100,default="")

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()