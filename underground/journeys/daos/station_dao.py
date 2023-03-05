from journeys import daos
from journeys.models import Station, TravelCharge


class StationDAO(daos.BaseDAO):
    model = Station


class TravelChargeDAO(daos.BaseDAO):
    model = TravelCharge
