from rest_framework.permissions import BasePermission
from .models import Staff

class IsStaffPermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return Staff.objects.filter(username=request.user.username).exists()
        return False

