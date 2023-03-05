from journeys.daos import station_dao
from accounts import constants as act_constants


# Later on will be shifted to configuration model in Django
# to avoid code deployment due to discount change
DISCOUNTS = {
    'Student card': 20,
    'Adult card': 0,
    'Senior card': 40
}


class Station:
    s_dao = station_dao.StationDAO
    tc_dao = station_dao.TravelChargeDAO

    @classmethod
    def get_stations(cls, columns: list, filters: dict = {}):
        return cls.s_dao.list_obj(**{
            'filters': filters,
            'columns': columns
        })
    
    @classmethod
    def get_ticket_charges_by_user_type(cls, origin, destination, columns: list, user_type=act_constants.ADULT_USER):
        tc_charges = cls.tc_dao.get_price(**{
            'filters': {'origin': origin, 'destination': destination},
            'columns': columns
        })
        for obj in tc_charges:
            obj['price'] -= ((obj['price'] * DISCOUNTS[user_type]) / 100)
        return tc_charges
