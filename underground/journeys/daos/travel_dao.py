from journeys import daos
from journeys.models import Journey, JourneyPayment


class JourneyDAO(daos.BaseDAO):
    model = Journey


class JourneyPaymentDAO(daos.BaseDAO):
    model = JourneyPayment
