from django.db import models

from accounts.models import MetroCard


class Station(models.Model):
    name = models.CharField(max_length=32)
    code = models.CharField(max_length=4)

    def __str__(self):
        return self.name


class TravelCharge(models.Model):
    '''
        For simplicity charges will be same at all times,
        to avoid many to many between stations due to time of day
    '''
    station_1 = models.ForeignKey(Station, blank=False, null=False, on_delete=models.CASCADE, related_name='station_1')
    station_2 = models.ForeignKey(Station, blank=False, null=False, on_delete=models.CASCADE, related_name='station_2')
    price = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f'{self.station_1.code}-{self.station_2.code}'


class Journey(models.Model):
    '''
        # on delete make it None, to do analysis on journeys
        # for simplicity only start time is captured for now
    '''
    origin = models.ForeignKey(Station, blank=False, null=True, on_delete=models.DO_NOTHING, related_name='origin')
    destination = models.ForeignKey(Station, blank=False, null=True, on_delete=models.DO_NOTHING, related_name='destination')
    metro_card = models.ForeignKey(MetroCard, blank=False, null=True, on_delete=models.DO_NOTHING)
    timestamp = models.DateTimeField(blank=False, null=False)

    def __str__(self):
        return f'{self.origin.code}-{self.destination.code}'


class JourneyPayment(models.Model):
    '''
        No checkin, checkout station price detection for now
    '''
    journey = models.ForeignKey(Journey, blank=False, null=False, on_delete=models.CASCADE)
    price = models.FloatField(null=False, blank=False)

    def __str__(self):
        return f'{self.journey}'
