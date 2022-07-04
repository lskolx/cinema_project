from rest_framework.permissions import BasePermission


class IsCommentAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        print(dir(obj))
        print(obj.author)
        print(request.user)
        return request.user.is_authenticated and obj.author == request.user
