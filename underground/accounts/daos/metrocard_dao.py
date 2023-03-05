from accounts import daos
from accounts.models import MetroCard


class MetroCardDAO(daos.BaseDAO):
    model = MetroCard

    @classmethod
    def deactivate_metrocard(cls, user_email: str):
        cls.model.objects.filter(
            userprofile__user__email=user_email
        ).update(
            is_active=False
        )
    
    @classmethod
    def activate_metrocard(cls, user_email: str):
        # Operation denied for now, remaining balance will
        # be settled manually
        raise NotImplementedError
