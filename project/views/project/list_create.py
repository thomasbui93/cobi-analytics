from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from project.models.project import Project
from project.serializers.project import ProjectSerializer
from common.pagination.small_result import SmallResultsSetPagination

class ProjectListCreateView(ListCreateAPIView):
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = SmallResultsSetPagination

    def get_queryset(self):
        user = self.request.user
        return Project.objects.filter(user = user)
