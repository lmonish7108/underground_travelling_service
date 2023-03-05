# import os

# from django.conf import settings
# from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
# from django.urls import reverse
from django.views import View

from journeys.services.station import Station
from accounts.services.metrocard import MetroCard



class BookJourney(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        stations = Station.get_stations(columns=['id', 'name', 'code'])
        metro_card_details = MetroCard.get_card_details(request.user.email)
        return render(request, 'journeys/book.html', {'stations': stations, 'balance': metro_card_details.balance})
    
    def post(self, request, *args, **kwargs):
        stations = Station.get_stations(columns=['id', 'name', 'code'])
        return render(request, 'journeys/book.html', {'stations': stations})


class TicketChargeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        origin = request.GET.get('origin')
        destination = request.GET.get('destination')
        metro_card_details = MetroCard.get_card_details(request.user.email)
        ticket_prices = Station.get_ticket_charges_by_user_type(
            origin, destination, columns=['station_1_id', 'station_2_id', 'price'], 
            user_type=metro_card_details.card_type
        )
        return JsonResponse(ticket_prices[0])