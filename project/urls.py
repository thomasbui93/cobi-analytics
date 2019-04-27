from django.conf.urls import url
from .views.project import ProjectView

urlpatterns = [
    url(r'^entry', ProjectView.as_view(), name='Project Entry Operation'),
]