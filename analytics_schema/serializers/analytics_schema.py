from rest_framework import serializers
import logging
from analytics_schema.models.analytics_schema import AnalyticsSchema
from project.models.project import Project

class AnalyticsSchemaSerializer(serializers.ModelSerializer):
    schema = serializers.JSONField(binary=True)

    class Meta:
        model = AnalyticsSchema
        exclude = []

    def validate(self, data):
        current_user = self.context['request'].user
        if (data['project'].user_id != current_user.id):
            raise serializers.ValidationError("Permission denied for modification.")
        return data
