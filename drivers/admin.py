from django.contrib import admin
from .models import BusRoute, Driver

# Register your models here.
admin.site.register(Driver)
admin.site.register(BusRoute)