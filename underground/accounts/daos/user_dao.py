from django.contrib.auth.models import User

from accounts import daos


class UserDAO(daos.BaseDAO):
    model = User