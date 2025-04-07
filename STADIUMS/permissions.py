from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsManagerOfStadion(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.managers.filter(user=request.user, approved_by_owner=True).exists()
