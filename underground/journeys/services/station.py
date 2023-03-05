from journeys.daos import station_dao


class Station:
    s_dao = station_dao.StationDAO

    @classmethod
    def get_stations(cls, columns: list, filters: dict = {}):
        return cls.s_dao.list_obj(**{
            'filters': filters,
            'columns': columns
        })
