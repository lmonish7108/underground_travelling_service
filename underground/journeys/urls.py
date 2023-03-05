from django.urls import path

from journeys.views import book_journey as journey_views

urlpatterns = [
    path('book/', journey_views.BookJourney.as_view(), name='book_journey'),
    path('ticket/price/', journey_views.TicketChargeView.as_view(), name='ticket_price'),
    path('myjourneys/', journey_views.UserJourneysView.as_view(), name='journeys'),
]