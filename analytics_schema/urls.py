from django.conf.urls import url
from .views.create import AnalyticsSchemaCreateView

urlpatterns = [
    url(r'^el', AnalyticsSchemaCreateView.as_view(), name='Create Operation'),
]