from rest_framework import permissions

from users.models import UserRoles


class IsSelectionOwnerOrAdmin(permissions.BasePermission):
    message = 'Access for selection editing is prohibited'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.owner or request.user.role in [UserRoles.ADMIN]:
            return True
        return False


class IsAdOwnerOrModerator(permissions.BasePermission):
    message = 'Access for selection editing is prohibited'

    def has_object_permission(self, request, view, obj):
        if request.user == obj.author or request.user.role in [UserRoles.MODERATOR, UserRoles.ADMIN]:
            return True
        return False
