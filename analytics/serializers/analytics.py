from rest_framework import serializers
import logging
from analytics.models.analytics import Analytics
from project.models.project import Project

class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analytics
        exclude = []