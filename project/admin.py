from django.contrib import admin

# Register your models here.

from .models.project import Project

admin.site.register(Project)