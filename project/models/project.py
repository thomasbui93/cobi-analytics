from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField('created date', auto_now_add=True)
    updated_date = models.DateTimeField('updated date', auto_now=True)

    def __str__(self):
        return self.title
