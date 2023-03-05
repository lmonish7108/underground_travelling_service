from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from accounts.services.metrocard import MetroCard
from journeys.services.station import Station
from journeys.services.ticket import TicketBooking
from journeys.services.journey import Journey
from journeys.forms import ticket_booking


class BookJourney(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        stations = Station.get_stations(columns=['id', 'name', 'code'])
        metro_card_details = MetroCard.get_card_details(request.user.email)
        return render(request, 'journeys/book.html', {'stations': stations, 'balance': metro_card_details.balance})
    
    def post(self, request, *args, **kwargs):
        metro_card_details = MetroCard.get_card_details(request.user.email)
        form = ticket_booking.TicketBookingForm(request.POST)
        if form.is_valid():
            ticket_details = TicketBooking.book_ticket(metro_card_details, form.cleaned_data)
            if ticket_details['msg'] == 'success':
                return HttpResponseRedirect(redirect_to=reverse('journeys'))
            return HttpResponse(ticket_details['msg'])
        return HttpResponse('Invalid request')


class TicketChargeView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        origin = request.GET.get('origin')
        destination = request.GET.get('destination')
        journey_type = request.GET.get('journey_type')
        metro_card_details = MetroCard.get_card_details(request.user.email)
        ticket_prices = Station.get_ticket_charges_by_user_type(
            origin, destination, journey_type, columns=['station_1_id', 'station_2_id', 'price'], 
            user_type=metro_card_details.card_type
        )
        return JsonResponse(ticket_prices[0])


class UserJourneysView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        metro_card_details = MetroCard.get_card_details(request.user.email)
        user_journeys = Journey.user_journeys(metro_card_details, ['origin__name', 'destination__name', 'journey_type'])
        return render(request, 'journeys/user_journeys.html', {'user_journeys': user_journeys})
