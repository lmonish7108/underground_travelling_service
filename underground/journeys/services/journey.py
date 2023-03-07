from journeys.daos import travel_dao


class Journey:
    t_dao = travel_dao.JourneyDAO

    @classmethod
    def user_journeys(self, metro_card_details, columns):
        return self.t_dao.list_obj(**{
            'filters': {
                'metro_card_id': metro_card_details.id
            },
            'columns': columns
        })
    
    @classmethod
    def all_journey_data(self, columns):
        self.t_dao.list_obj(**{'filters': {},'columns': columns})
