from rest_framework import permissions


class IsModerator(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.groups.filter(name='moderator').exists():
            return True
