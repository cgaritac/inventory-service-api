from rest_framework.permissions import BasePermission
from apps.users.models import User

class IsOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [
            User.Role.OWNER,
            User.Role.ADMIN
        ]
    
class IsManagerOrAbove(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in [
            User.Role.OWNER,
            User.Role.ADMIN,
            User.Role.MANAGER
        ]