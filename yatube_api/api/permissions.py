from rest_framework import permissions


class AuthorAccessPermission(permissions.BasePermission):
    message = 'Удаление чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
