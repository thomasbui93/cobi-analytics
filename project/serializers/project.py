from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from project.models.project import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ('user', )

    def create(self, validated_data):
        current_user = self.context['request'].user
        project = Project.objects.create(user=current_user, **validated_data)
        return project