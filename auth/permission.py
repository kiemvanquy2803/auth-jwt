from rest_framework.permissions import BasePermission


class IsUser(BasePermission):
    message = "Require User role."

    def has_permission(self, request, view):
        return request.user.id and (request.user.is_active or request.user.is_admin)