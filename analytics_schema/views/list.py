from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import PermissionDenied
from analytics_schema.models.analytics_schema import AnalyticsSchema
from analytics_schema.serializers.analytics_schema import AnalyticsSchemaSerializer
from project.models.project import Project
from common.pagination.small_result import SmallResultsSetPagination

class AnalyticsSchemaListView(ListAPIView):
    serializer_class = AnalyticsSchemaSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        project_id = self.kwargs['pk']
        user_id = self.request.user.id
        project = Project.objects.get(id=project_id, user_id=user_id)

        if (project == None):
            raise PermissionDenied('Permission denied')

        return AnalyticsSchema.objects.filter(project_id=project_id)