from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

# Create your views here.
@api_view(['GET'])
def all_routes(request):
    api_urls = {
        "User Registration":"auth/register/",
        "User Login": "auth/token/",
        "Refresh Tokens": "auth/token/refresh/",
        "Update isDriver Status": "auth/driver_status/",
        "Convert Address to LatLng": "geo/get_places/",
        "Convert LatLng to Address": "geo/decode_latlang/",
        "Autocomplete Places on Search": "geo/autocomplete/",
        "Update Bus Number": "driver/update/details/",
        "Get Bus/Driver Details": "driver/get/details/",
        "Update Bus Route": "driver/route/",
        "Get Bus Route": "driver/get/route/",
        "Passenger Travel History": "passenger/history/",
    }
    return Response(api_urls)