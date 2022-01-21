from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
# import googlemaps
import requests
from urllib.parse import urlencode
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def geo_routes(request):
    api_urls = {
        'List': '/member-list/',
        'Create': '/member-create/'
    }
    return Response(api_urls)


@api_view(['GET'])
def test(request):
    data_type = "json"
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address":"Habra Railwa Station","key":"AIzaSyCbtnaXLB2psoXbWRecZrgV2bDDOr_LdrA"}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    print(url)
    res = requests.get(url)
    print(res.json()["results"])
    if not res.status_code in range(200,299):
        return {}
    return Response(res.json())


@api_view(['GET'])
def get_places(request):
    query = request.data["query"]
    print(query)
    data_type = "json"
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"address":f"{query}","key":"AIzaSyC3Ml4YLtU58N72tqHQVDzM37r61vdbZWY"}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    print(url)
    res = requests.get(url)
    print(res.json()["results"])
    if not res.status_code in range(200,299):
        return {}
    return Response(res.json()["results"])


@api_view(['GET','POST'])
def decode_latlang(request):
    lat = request.data["lat"]
    lng = request.data["lng"]
    data_type = "json"
    endpoint = f"https://maps.googleapis.com/maps/api/geocode/{data_type}"
    params = {"latlng":f"{lat},{lng}","key":"AIzaSyC3Ml4YLtU58N72tqHQVDzM37r61vdbZWY"}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    res = requests.get(url)
    if not res.status_code in range(200,299):
        return {}
    return Response(res.json())


@api_view(['GET'])
def autocomplete(request):
    lat = request.data["lat"]
    lng = request.data["lng"]
    query = request.data["query"]
    data_type = "json"
    endpoint = f"https://maps.googleapis.com/maps/api/place/autocomplete/{data_type}"
    params = {"location":f"{lat},{lng}","key":"AIzaSyC3Ml4YLtU58N72tqHQVDzM37r61vdbZWY","input":f"{query}"}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    print(url)
    res = requests.get(url)
    if not res.status_code in range(200,299):
        return {}
    return Response(res.json())


@api_view(['GET'])
def place_details_from_id(request):
    place_id = request.data["place_id"]
    data_type = "json"
    endpoint = f"https://maps.googleapis.com/maps/api/place/details/{data_type}"
    params = {"place_id":f"{place_id}","key":"AIzaSyC3Ml4YLtU58N72tqHQVDzM37r61vdbZWY"}
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"
    print(url)
    res = requests.get(url)
    if not res.status_code in range(200,299):
        return {}
    return Response(res.json())