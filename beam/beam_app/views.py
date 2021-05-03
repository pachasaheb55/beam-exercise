from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Location
from django.conf import settings
import json, requests


# Create your views here.
def exercise1_beam(request):
    context = {}
    return render(request,'exercise1.html',context)

def exercise2_beam(request):
    context = {}
    return render(request,'exercise2.html',context)

@csrf_exempt
def save_scooters(request):
    if request.method == "POST":
        input_data = json.loads(request.body)
        location = Location.objects.create(latitude=input_data['lat'],
                                        longitude=input_data['long'],
                                        scooters=input_data['scooters'])
        return HttpResponse("Location Saved Successfully")


def calculate_distance(url, distance):
    response = requests.get(url)
    if response.status_code == 200:
        response_dict = response.json()
        if response_dict['status'] == 'OK':
            if response_dict['rows'][0]['elements'][0]['distance']['value'] < distance:
                return True, 'success'
            else:
                return False, 'success'
        else:
            return False, 'error'

def nearby_scooters(locations, lat, lng, distance):
    matched_loc = {}
    matched_loc['scooters_count'] = 0
    result = []
    for loc in locations:
        maps_api_url = f'{settings.MAPS_URL}?origins={lat},{lng}' \
                        f'&destinations={loc["latitude"]},{loc["longitude"]}' \
                        f'&mode=walking&key={settings.MAPS_API_KEY}'
        maps_distance, status = calculate_distance(maps_api_url, distance)
        if maps_distance and status == 'success':
            result.append(loc)
            matched_loc['scooters_count'] += loc["scooters"]
    matched_loc['result'] = result
    matched_loc['locations_count'] = len(result)
    return JsonResponse(matched_loc, safe=False) 


@csrf_exempt
def search_scooters(request, lat, long, distance, measurement):
    if request.method == "GET":
        print(lat, long, distance, measurement)
        if measurement == 'km': distance *= 1000
        if measurement == 'mile': distance *= 1609.34
        locations = Location.objects.values()
        return nearby_scooters(locations, lat, long, distance)

            
        


@csrf_exempt
def retrieve_scooters(request):
    if request.method == "GET":
        locations = list(Location.objects.values())
        return JsonResponse(locations, safe=False) 

                
