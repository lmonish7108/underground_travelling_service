# import os

# from django.conf import settings
# from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
# from django.urls import reverse
from django.views import View

# from accounts.services.google import GoogleOnboarding
# from accounts.services.user import UserOnboarding
# from accounts import utils as act_utils


class BookJourney(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'journeys/book.html')
