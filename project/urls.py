from django.conf.urls import url
from .views.project.list_create import ProjectListCreateView
from .views.project.read_update_delete import ProjectReadUpdateDeleteView

urlpatterns = [
    url(r'^el', ProjectListCreateView.as_view(), name='List Or Create Operation'),
    url(r'^e/(?P<pk>\d+)', ProjectReadUpdateDeleteView.as_view(), name='RUD Operation'),
]