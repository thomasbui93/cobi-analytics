import uuid
from django.db import models
from project.models.project import Project

class AnalyticsSchema(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200, null=False)
    schema = models.TextField(null=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_date = models.DateTimeField('created date', auto_now_add=True)
    updated_date = models.DateTimeField('updated date', auto_now=True)

    def __str__(self):
        return self.title