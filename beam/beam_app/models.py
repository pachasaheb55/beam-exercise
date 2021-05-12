from django.db import models

class Location(models.Model):
    """Location table for Scooter Locations"""
    latitude = models.DecimalField(max_digits=9, unique=True, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, unique=True, decimal_places=6)
    scooters = models.IntegerField(default=0)
