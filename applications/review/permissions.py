from rest_framework.permissions import BasePermission


class IsReviewAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_authenticated and obj.user == request.user


