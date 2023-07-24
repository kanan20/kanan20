from rest_framework import permissions

class IsPostOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsLikeOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user