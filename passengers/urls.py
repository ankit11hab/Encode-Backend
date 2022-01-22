from django.urls import path
from . import views

urlpatterns = [
    path('', views.passenger_routes, name='passenger-routes'),
    path('history/', views.passenger_history, name='passenger-history'),
    path('active/', views.get_active_bookings, name='active-bookings'),
]