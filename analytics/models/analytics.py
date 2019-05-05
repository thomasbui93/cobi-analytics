import uuid
from django.db import models
from project.models.project import Project

class Analytics(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    data = models.TextField(null=False, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_date = models.DateTimeField('created date', auto_now_add=True)