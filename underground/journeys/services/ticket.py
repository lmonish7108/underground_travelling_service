from django.utils import timezone

from accounts.daos import metrocard_dao
from journeys.services.station import Station
from journeys.daos import travel_dao


class TicketBooking:
    t_dao = travel_dao.JourneyDAO
    tp_dao = travel_dao.JourneyPaymentDAO
    mc_dao = metrocard_dao.MetroCardDAO

    @classmethod
    def book_ticket(cls, metro_card_details, ticket_details):
        # Get ticket price
        ticket_price = Station.get_ticket_charges_by_user_type(
            origin=ticket_details['origin'],
            destination=ticket_details['destination'],
            journey_type=ticket_details['journey_type'],
            columns=['station_1_id', 'station_2_id', 'price'],
            user_type=metro_card_details.card_type
        )[0]

        if ticket_price['price'] > metro_card_details.balance:
            return {'msg': 'Insufficient balance, kindle recharge metrocard'}
        else:
            cls.mc_dao.deduct_ticket_money(metro_card_details, ticket_price['price'])
        
        journey = cls.t_dao.create_obj(
            **{
                'origin_id': ticket_details['origin'],
                'destination_id': ticket_details['destination'],
                'journey_type': ticket_details['journey_type'],
                'metro_card_id': metro_card_details.id,
                'timestamp': timezone.now()
            }
        )

        cls.tp_dao.create_obj(
            **{
                'journey_id': journey.id,
                'price': ticket_price['price']
            }
        )
        return {'journey': journey, 'msg': 'success'}
