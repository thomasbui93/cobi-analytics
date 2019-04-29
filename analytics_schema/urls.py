from django.conf.urls import url
from .views.create import AnalyticsSchemaCreateView
from .views.list import AnalyticsSchemaListView
from .views.read_update_delete import SchemaReadUpdateDeleteView

urlpatterns = [
    url(r'^el', AnalyticsSchemaCreateView.as_view(), name='Create Operation'),
    url(r'^ep/(?P<pk>[0-9a-f-]+)', AnalyticsSchemaListView.as_view(), name='Schema list from project'),
    url(r'^e/(?P<pk>[0-9a-f-]+)', SchemaReadUpdateDeleteView.as_view(), name='Schema rud'),
]