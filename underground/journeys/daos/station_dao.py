from journeys import daos
from journeys.models import Station, TravelCharge
from django.db.models import Q


class StationDAO(daos.BaseDAO):
    model = Station


class TravelChargeDAO(daos.BaseDAO):
    model = TravelCharge

    @classmethod
    def get_price(cls, **kwargs):
        return cls.model.objects.filter(
            Q(station_1_id=kwargs.get('filters')['origin'], station_2_id=kwargs.get('filters')['destination']) | 
            Q(station_2_id=kwargs.get('filters')['origin'], station_1_id=kwargs.get('filters')['destination']) 
        ).values(*kwargs['columns'])
