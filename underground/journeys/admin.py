from django.contrib import admin
from journeys import models as j_models

admin.site.register(j_models.Journey)
admin.site.register(j_models.JourneyPayment)
admin.site.register(j_models.Station)
admin.site.register(j_models.TravelCharge)
