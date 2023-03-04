from accounts import models as act_models
from accounts import daos


class GoogleRequestDAO(daos.BaseDAO):
    model = act_models.GoogleRequest


class SocialProfileDAO(daos.BaseDAO):
    model = act_models.SocialProfile