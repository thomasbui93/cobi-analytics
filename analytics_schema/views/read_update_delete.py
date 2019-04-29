from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from project.models.project import Project
from analytics_schema.models.analytics_schema import AnalyticsSchema
from analytics_schema.serializers.analytics_schema import AnalyticsSchemaSerializer
from analytics_schema.permissions.schema_owner import SchemaOwner
from project.serializers.project import ProjectSerializer

class SchemaReadUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    serializer_class = AnalyticsSchemaSerializer
    queryset = AnalyticsSchema.objects.all()
    permission_classes = (IsAuthenticated, SchemaOwner,)