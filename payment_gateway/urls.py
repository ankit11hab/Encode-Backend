from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_routes, name='purchase-routes'),
    path('test/', views.test_payment, name='test-payment'),
    path('success/', views.success, name='payment-success'),
    path('history/', views.payment_history, name='payment-history'),
]