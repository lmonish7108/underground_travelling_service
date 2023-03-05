from django.urls import path

from accounts.views import signup as signup_views

urlpatterns = [
    path('google/callback/', signup_views.GoogleCallback.as_view(), name='google_callback'),
    path('signup/', signup_views.GoogleLoginView.as_view(), name='signup'),
    path('onboarding/', signup_views.UserSignupComplete.as_view(), name='onboard')
]