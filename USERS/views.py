from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, UserInfoSerializer



User = get_user_model()


class UserListView(LoginRequiredMixin, generics.ListCreateAPIView):
    """
    API view to retrieve a list of all users and create new users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]  # Only admin users can access this view

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserDetailView(LoginRequiredMixin,generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a user.
    """
    queryset = User.objects.all()
    serializer_class = UserInfoSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access this view

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a specific user.
        """
        return super().get(request, *args, **kwargs)
    
