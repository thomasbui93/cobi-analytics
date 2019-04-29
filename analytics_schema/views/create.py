from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from analytics_schema.models.analytics_schema import AnalyticsSchema
from analytics_schema.serializers.analytics_schema import AnalyticsSchemaSerializer
from project.models.project import Project
from project.permissions.project_owner import ProjectOwner
from common.pagination.small_result import SmallResultsSetPagination

class AnalyticsSchemaCreateView(CreateAPIView):
    serializer_class = AnalyticsSchemaSerializer
    permission_classes = (IsAuthenticated,ProjectOwner,)
    pagination_class = SmallResultsSetPagination