import os

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import render

from accounts.services.google import GoogleOnboarding
from accounts import utils as act_utils


class GoogleCallback(View):
    template_name = 'accounts/complete_signup.html'

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        state = request.GET.get('state')
        social_profile = GoogleOnboarding().onboard_user(authorization_code=code, state=state)
        return render(request, self.template_name, context={**social_profile})


class UserOnboarding(View):

    def post(self, request, *args, **kwargs):
        print(request.POST)
        return HttpResponse("testing")


class HomepageView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/index.html')


class GoogleLoginView(View):
    template_name = 'accounts/google_login.html'

    def get(self, request, *args, **kwargs):
        context = {
            'google_oauth_login': f'https://accounts.google.com/o/oauth2/auth?response_type=code&redirect_uri={os.getenv("GOOGLE_OAUTH2_REDIRECT_URI")}&client_id={os.getenv("GOOGLE_CLIENT_ID")}&scope=https://www.googleapis.com/auth/userinfo.email&state={act_utils.generate_state()}'
        }
        return render(request, self.template_name, context)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')
