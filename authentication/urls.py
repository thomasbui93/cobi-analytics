from django.urls import path
from .views import auth as auth_view

urlpatterns = [
    path('sign-in', auth_view.sign_in_action, name='Sign In'),
    path('sign-up', auth_view.sign_up_action, name='Sign Up'),
    path('sign-out', auth_view.sign_out_action, name='Sign Out'),
    path('me', auth_view.get_me_action, name='User Profile'),
]