from django import forms


class TicketBookingForm(forms.Form):
    origin = forms.IntegerField(required=True)
    destination = forms.IntegerField(required=True)
    journey_type = forms.CharField(required=True)
