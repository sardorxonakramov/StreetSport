from rest_framework import generics, status
from django.urls import reverse_lazy
from rest_framework.permissions import IsAdminUser
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .serializers import RegisterSerializer, LoginSerializer, UserSerializer, UserInfoSerializer



User = get_user_model()
class UserListView(LoginRequiredMixin,generics.ListAPIView):
    """
    API view to retrieve a list of all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [IsAdminUser]  # Only admin users can access this view
    success_url = reverse_lazy('userlist')
    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve the list of users.
        """
        return super().get(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        """
        Handle POST requests to create a new user.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return reverse_lazy('userlist')


class UserDetailView(LoginRequiredMixin,UserPassesTestMixin,generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser]  # Only admin users can access this view

    def get(self, request, *args, **kwargs):
        """
        Handle GET requests to retrieve a specific user.
        """
        return super().get(request, *args, **kwargs)