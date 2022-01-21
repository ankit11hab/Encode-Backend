from django.urls import path,include
from . import views
from .views import MyTokenObtainPairView, RegisterView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
    path('', views.routes, name='routes'),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/',RegisterView.as_view(),name='register'),
    path('get_profile/',views.get_profile,name='get-profile'),
    path('driver_status/',views.driver_status,name='driver-status'),
    path('check_username_exists/',views.check_username_exists,name='check-username-exists'),
]
