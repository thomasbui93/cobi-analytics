from project.models.project import Project
from django.shortcuts import get_object_or_404
from analytics_schema.models.analytics_schema import AnalyticsSchema

def validate_ip(ip, project_id):
    project = get_object_or_404(Project, id = project_id)

    if ip == '':
        return False

    if project.ips == '':
        return True
    else:
        ips = project.ips.split(',')
        return ips.index(ip) > -1


def validate_data(ip, project_id):
    return validate_ip(ip, project_id)