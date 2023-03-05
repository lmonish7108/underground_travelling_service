from django.urls import path

from journeys.views import book_journey as journey_views

urlpatterns = [
    path('book/', journey_views.BookJourney.as_view(), name='book_journey'),
]