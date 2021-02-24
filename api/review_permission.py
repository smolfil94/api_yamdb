from rest_framework import permissions


class IsModeratorOrAdminOrAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return (
                request.user == obj.author or
                request.user.role in ['admin', 'moderator']
            )
        return request.method in permissions.SAFE_METHODS
