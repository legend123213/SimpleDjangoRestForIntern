from rest_framework.permissions import BasePermission


class IsInGroup(BasePermission):
    def has_permission(self, request, view):
        required_group = 'user_permission'  # Replace with the group name you want to check
        return request.user.groups.filter(name=required_group).exists()
