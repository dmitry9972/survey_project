from rest_framework import permissions


class AdminPermission(permissions.BasePermission):
    def has_permission(self, request, view):


        if view.action in ['create', 'update', 'partial_update', 'destroy', ]:
            return request.user.is_authenticated and request.user.is_staff
        elif view.action in ['list', 'retrieve']:
            return True
        else:
            return False