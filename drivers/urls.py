from django.urls import path
from . import views

urlpatterns = [
    path('', views.driver_routes, name='driver-routes'),
    path('update/details/', views.driver_details, name='driver-details'),
    path('get/details/', views.get_driver_details, name='get-driver-details'),
    path('new/route/', views.new_bus_route, name='new-bus-route'),
    path('get/buses/', views.get_buses, name='get-buses'),
    path('get/bus/', views.get_bus_description, name='get-bus-description'),
    path('book/', views.book_ticket, name='book-ticket'),
    path('route/', views.bus_route, name='bus-route'),
]