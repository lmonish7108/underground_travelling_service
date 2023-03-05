from accounts.daos import metrocard_dao
from accounts import utils


class MetroCard:
    mc_dao = metrocard_dao.MetroCardDAO

    @classmethod
    def create_metrocard(self, user_profile):
        metrocard_obj = {
            'userprofile_id': user_profile.id,
            # Assuming user has paid in advance
            # feature to be developed
            'balance': 30,
            'is_active': True,
            'card_id': utils.generate_state()
        }
        self.mc_dao.deactivate_metrocard(user_profile.user.email)
        self.mc_dao.create_obj(**metrocard_obj)
        return 'Metro card created successfully'
    
    @classmethod
    def get_card_details(self, email):
        return self.mc_dao.get_obj(**{'userprofile__user__email': email})
