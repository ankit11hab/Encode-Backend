from django.urls import path
from . import views

urlpatterns = [
    path('', views.geo_routes, name='geo-routes'),
    path('test/', views.test, name='test'),
    path('get_places/', views.get_places, name='get-places'),
    path('decode_latlang/', views.decode_latlang, name='decode-latlang'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('place_details_from_id/', views.place_details_from_id, name='place_details_from_id'),
]