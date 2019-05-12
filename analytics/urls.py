from django.urls import path
from .views.create import create_action

urlpatterns = [
    path('ping', create_action, name='Data acquire endpoint'),
]