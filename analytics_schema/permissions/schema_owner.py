from rest_framework import permissions
from project.models.project import Project

class SchemaOwner(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        user_id = request.user.id
        project_id = obj.project_id
        project = Project.objects.filter(id=project_id, user_id=user_id)

        return project != None