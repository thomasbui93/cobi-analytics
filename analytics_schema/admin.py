from django.contrib import admin

# Register your models here.
from .models.analytics_schema import AnalyticsSchema

admin.site.register(AnalyticsSchema)