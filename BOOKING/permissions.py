# from .permissions import IsManager
# from rest_framework import permissions,generics,serializers
# from STADIUMS.serializers import StadionBookingSerializer
# from .models import StadionBooking


# class ManagerStadionOfflineBookingView(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated, IsManager]
#     serializer_class = StadionBookingSerializer

#     def perform_create(self, serializer):
#         stadion = serializer.validated_data['stadion']
#         if StadionBooking.objects.filter(stadion=stadion, is_active=True).exists():
#             raise serializers.ValidationError("Bu stadion allaqachon band!")
#         serializer.save(user=self.request.user, is_offline=True)


from rest_framework.permissions import BasePermission


class IsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'manager'
