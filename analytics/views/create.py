from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.http import JsonResponse, HttpResponse
from analytics.models.analytics import Analytics
from analytics.services.ip import get_ip_from_request
from analytics.services.data_validate import validate_ip
from project.models.project import Project

@csrf_exempt
@api_view(['POST'])
def create_action(request):
    try:
        project_id = request.GET.get('key')
        project = Project.objects.get(id = project_id)
    except Project.DoesNotExist:
        return JsonResponse({'message': 'Invalid key.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        encoded_data = request.POST.get('data')
        ip = get_ip_from_request(request)
        
        if not validate_ip(ip, project_id):
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        
        data = Analytics.objects.create(data = encoded_data, ip = ip, project_id = project_id)
        return HttpResponse(status=status.HTTP_201_CREATED)
    except BaseException:
        return HttpResponse(status=status.HTTP_400_BAD_REQUEST)