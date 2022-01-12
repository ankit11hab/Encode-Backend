from django.urls import path
from . import views

urlpatterns = [
    path('', views.driver_routes, name='driver-routes'),
    path('update/details/', views.driver_details, name='driver-details'),
    path('get/details/', views.get_driver_details, name='get-driver-details'),
    path('get/route/', views.get_bus_route, name='get-bus-route'),
    path('route/', views.bus_route, name='bus-route'),
]