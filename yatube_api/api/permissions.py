from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthorOrReadOnly(BasePermission):
    """Только владелец может редактировать и удалять"""
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS or request.user.is_authenticated:
            return True
        return obj.author == request.user