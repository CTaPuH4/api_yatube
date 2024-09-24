from rest_framework import permissions


class AuthorAccessPermission(permissions.BasePermission):
    message = 'Изменение/удаление чужого контента запрещено!'

    def has_object_permission(self, request, view, obj):
        return request.method == 'GET' or obj.author == request.user
