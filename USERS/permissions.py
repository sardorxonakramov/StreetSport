from rest_framework.permissions import BasePermission


class UserViewUchunRuxsatlar(BasePermission):
    """
    Foydalanuvchi is_staff bo'lsa yoki role == 'admin' bo'lsa ruxsat beriladi.
    """

    def has_permission(self, request, view):
        return bool(
            request.user
            and request.user.is_authenticated
            and (request.user.is_staff or request.user.role == "admin")
        )
