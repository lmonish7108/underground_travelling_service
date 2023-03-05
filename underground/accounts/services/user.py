from accounts.daos import user_dao, metrocard_dao
from accounts import utils

class UserOnboarding:
    u_dao = user_dao.UserDAO
    up_dao = user_dao.UserProfileDAO
    mc_dao = metrocard_dao.MetroCardDAO

    def onboard_user(self, user_details: dict):
        user_obj = {
            'email': user_details['email'],
            'defaults': {
                'username': user_details['first_name'],
                'first_name': user_details['first_name'],
                'last_name': user_details['last_name'],
                'is_active': True
            }
        }
        self.u_dao.update_or_create_obj(**user_obj)
        # user profile
        user_obj = self.u_dao.get_obj(**{'email': user_details['email']})
        user_profile_obj = {
            'user_id': user_obj.id,
            'defaults': {
                'address': user_details['address'],
                'mobile': user_details['mobile'],
                'age': int(user_details['age'])
            }
        }
        self.up_dao.update_or_create_obj(**user_profile_obj)
        # Create metrocard after deactivating existing
        # remaining balances will be settled manually
        user_profile_obj = self.up_dao.get_obj(**{'user__email': user_details['email']})
        metrocard_obj = {
            'userprofile_id': user_profile_obj.id,
            # Assuming user has paid in advance
            # feature to be developed
            'balance': 20,
            'is_active': True,
            'card_id': utils.generate_state()
        }
        self.mc_dao.deactivate_metrocard(user_details['email'])
        self.mc_dao.create_obj(**metrocard_obj)
        return {'user': self.u_dao.get_obj(email=user_details['email']), 'msg': 'success'}
