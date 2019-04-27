from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from project.models.project import Project
from project.serializers.project import ProjectSerializer
from common.pagination.small_result import SmallResultsSetPagination

class ProjectListCreateView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = (IsAuthenticated,)
    pagination_class = SmallResultsSetPagination
