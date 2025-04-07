from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    UserInfoSerializer,
)
from .permissions import UserViewUchunRuxsatlar

User = get_user_model()


class UserListView(generics.ListCreateAPIView):
    """Api orqali userlarni json ko'rinishida ko'rish uchun view"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        IsAuthenticated,
        UserViewUchunRuxsatlar
    ]  
    ordering = ["-created_at"]

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetailView(UserPassesTestMixin, generics.RetrieveUpdateDestroyAPIView):
    """API lar orqali userni update yoki delete qilishi mumkin"""

    queryset = User.objects.all()
    serializer_class = UserInfoSerializer

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a specific user.
        """
        return super().get(request, *args, **kwargs)

    def test_func(self):
        user = self.get_object()
        current_user = self.request.user

        return (
            current_user.is_superuser
            or current_user.is_staff
            or current_user.role == "admin"
            or current_user == user
        )


class UserRegisterView(generics.CreateAPIView):
    '''Userni ro'yxatdan o'tkazish uchun API view'''
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            {
                "message": "User registered successfully",
                "user": {
                    "id": user.id,
                    "email": user.email,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "phone": user.phone,
                    "role": user.role,
                },
            },
            status=status.HTTP_201_CREATED,
        )
