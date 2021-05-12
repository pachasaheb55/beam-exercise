"""Views file for the apis"""
import json
import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.db import IntegrityError
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Location


# Create your views here.
def exercise1_beam(request):
    """renders exercise1 html page"""
    return render(request,'exercise1.html')


def exercise2_beam(request):
    """renders exercise2 html page"""
    return render(request,'exercise2.html')

def exercise3_beam(request):
    """renders exercise3 html page"""
    return render(request,'exercise3.html')


@csrf_exempt
def save_scooters(request):
    """View to save the scooter Locations"""
    response = ''
    if request.method == "POST":
        try:
            input_data = json.loads(request.body)
            # Creating a Location Object
            location = Location.objects.create(latitude=input_data['lat'],
                                    longitude=input_data['long'],
                                    scooters=input_data['scooters'])
            response = f"Location Id {location.id} successfully created."
        except IntegrityError:
            response = "Given Latitude and Longitude already Exists."
        except Exception as exception:
            response = exception
    else:
        response = 'Only POST methods are allowed'
    return HttpResponse(response)


def calculate_distance(url, distance):
    """Definition to calculate the distance"""
    nearby = False
    status = ''
    # Making a GET call to Google Maps API
    response = requests.get(url)
    if response.status_code == 200:
        # converting json to dict
        response_dict = response.json()
        if response_dict['status'] == 'OK':
            # comparing the distance
            if response_dict['rows'][0]['elements'][0]['distance']['value'] < distance:
                nearby = True
                status = 'success'
            else:
                status = 'success'
        else:
            status = response_dict['status']
    else:
        status = response.json()['message']
    return nearby, status


def nearby_scooters(locations, lat, lng, distance):
    """method to make list of nearby scooter locations"""
    matched_loc = {}
    matched_loc['scooters_count'] = 0
    result = []
    # iterationg multiple locations
    for loc in locations:
        # Making a google maps api url to calculate the ditance
        maps_api_url = f'{settings.MAPS_URL}?origins={lat},{lng}' \
                        f'&destinations={loc["latitude"]},{loc["longitude"]}' \
                        f'&mode=walking&key={settings.MAPS_API_KEY}'
        # returs status and nearby flag
        nearby, status = calculate_distance(maps_api_url, distance)
        if nearby and status == 'success':
            result.append(loc)
            matched_loc['scooters_count'] += loc["scooters"]
    matched_loc['result'] = result
    matched_loc['locations_count'] = len(result)
    # returns JSON response with all the details
    return JsonResponse(matched_loc, safe=False)


@csrf_exempt
def search_scooters(request, lat, long, distance, measurement):
    """search scooters for the given parameters"""
    try:
        response = ''
        if request.method == "GET":
            if measurement == 'km':
                distance *= 1000
            elif measurement == 'mile':
                distance *= 1609.34
            locations = Location.objects.values()
            response = nearby_scooters(locations, lat, long, distance)
        else:
            response = HttpResponse("Only GET calls Permitted.")
        return response
    except Exception as error:
        return HttpResponse(error)


@csrf_exempt
def retrieve_scooters(request):
    """retrieve all scooter locations"""
    try:
        response = ''
        if request.method == "GET":
            locations = list(Location.objects.values())
            response = JsonResponse(locations, safe=False)
        else:
            response = HttpResponse("Only GET calls are permitted.")
        return response
    except Exception as error:
        return HttpResponse(error)
