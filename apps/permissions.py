from rest_framework.permissions import BasePermission

from apps.models import VacancyModel


class Auther(BasePermission):
    def has_object_permission(self, request, view, obj: VacancyModel):
        return request.user == obj.user
