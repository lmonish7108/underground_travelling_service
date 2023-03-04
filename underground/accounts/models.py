from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator

from accounts import constants as act_constants


class UserProfile(models.Model):
    '''
        # children upto age of 5 can travel for free
        # Not using birthdate field to keep it simple
        # on delete cascade user data for GDPR
    '''
    user = models.OneToOneField(User, null=False, blank=False, on_delete=models.CASCADE)
    address = models.TextField(null=False, blank=False, validators=[MaxLengthValidator(128)])
    mobile = models.TextField(null=False, blank=False)
    
    age = models.IntegerField(null=False, blank=False, validators=[MinValueValidator(6)])

    def __str__(self) -> str:
        return self.user


class MetroCard(models.Model):
    '''
        # If user's age changes, we will generate new metro card
        # to help data analysis on age and journeys
        # At any time only 1 metrocard will be active
        # on delete make it None, to do analysis on metro card
    '''
    user = models.ForeignKey(UserProfile, null=True, blank=False, on_delete=models.DO_NOTHING)
    card_id = models.UUIDField(null=False, blank=False)
    # Maximum balance to be 100, to avoid money exploitation
    balance = models.IntegerField(null=False, blank=False, validators=[MaxValueValidator(100)])
    is_active = models.BooleanField(default=False, null=True, blank=False)

    @property
    def card_type(self):
        if self.user.age > 5 and self.user.age < 19:
            return act_constants.STUDENT_USER
        elif self.user.age > 18 and self.user.age < 50:
            return act_constants.ADULT_USER
        else:
            return act_constants.SENIOR_USER
    
    def __str__(self) -> str:
        return self.user
