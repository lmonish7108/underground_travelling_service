# import os

# from django.conf import settings
# from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from django.urls import reverse
from django.views import View

from journeys.services.station import Station
# from accounts.services.user import UserOnboarding
# from accounts import utils as act_utils


class BookJourney(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        stations = Station.get_stations(columns=['id', 'name', 'code'])
        # metro_card_details = St
        return render(request, 'journeys/book.html', {'stations': stations})
    
    def post(self, request, *args, **kwargs):
        stations = Station.get_stations(columns=['id', 'name', 'code'])
        return render(request, 'journeys/book.html', {'stations': stations})
