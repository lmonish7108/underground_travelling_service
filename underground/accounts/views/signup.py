import os

from django.conf import settings
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from accounts.services.google import GoogleOnboarding
from accounts.services.user import UserOnboarding
from accounts import utils as act_utils
from accounts.forms import complete_signup


class GoogleCallback(View):
    template_name = 'accounts/complete_signup.html'

    def get(self, request, *args, **kwargs):
        code = request.GET.get('code')
        state = request.GET.get('state')
        social_profile = GoogleOnboarding().onboard_user(authorization_code=code, state=state)
        app_profile = UserOnboarding.get_user(social_profile['email'])
        if app_profile:
            login(request, app_profile, backend=settings.AUTHENTICATION_BACKENDS[0])
            return HttpResponseRedirect(redirect_to=reverse('book_journey'))
        form = complete_signup.CompleteSignupForm(initial={'email':social_profile['email']})
        return render(request, self.template_name, context={'complete_signup_form': form})


class UserSignupComplete(View):

    def post(self, request, *args, **kwargs):
        form = complete_signup.CompleteSignupForm(request.POST)
        if form.is_valid():
            app_profile = UserOnboarding().onboard_user(form.cleaned_data)
            if app_profile['msg'] == 'success':
                login(request, app_profile['user'], backend=settings.AUTHENTICATION_BACKENDS[0])
        return HttpResponseRedirect(redirect_to=reverse('book_journey'))


class SocialLoginView(View):
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        context = {
            'google_oauth_login': f'https://accounts.google.com/o/oauth2/auth?response_type=code&redirect_uri={os.getenv("GOOGLE_OAUTH2_REDIRECT_URI")}&client_id={os.getenv("GOOGLE_CLIENT_ID")}&scope=https://www.googleapis.com/auth/userinfo.email&state={act_utils.generate_state()}'
        }
        return render(request, self.template_name, context)


class LogoutView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(redirect_to=reverse('logout'))

