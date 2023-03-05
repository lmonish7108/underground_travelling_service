from accounts import daos
from accounts.models import User, UserProfile


class UserDAO(daos.BaseDAO):
    model = User


class UserProfileDAO(daos.BaseDAO):
    model = UserProfile
