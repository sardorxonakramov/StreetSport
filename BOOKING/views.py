from rest_framework import generics, permissions, serializers
from .models import StadionBooking
from .serializers import StadionBookingSerializer
from .permissions import IsManager


class StadionBookingCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StadionBookingSerializer

    def perform_create(self, serializer):
        stadion = serializer.validated_data['stadion']
        if StadionBooking.objects.filter(stadion=stadion, is_active=True).exists():
            raise serializers.ValidationError("Bu stadion allaqachon band!")
        serializer.save(user=self.request.user, is_offline=False)


class ManagerStadionOfflineBookingView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsManager]
    serializer_class = StadionBookingSerializer

    def perform_create(self, serializer):
        stadion = serializer.validated_data['stadion']
        if StadionBooking.objects.filter(stadion=stadion, is_active=True).exists():
            raise serializers.ValidationError("Bu stadion allaqachon band!")
        serializer.save(user=self.request.user, is_offline=True)


from rest_framework import generics, permissions
from STADIUMS.models import Stadion
from STADIUMS.serializers import StadionListSerializer


class PublicActiveStadionListView(generics.ListAPIView):
    queryset = Stadion.objects.filter(is_active=True)
    serializer_class = StadionListSerializer
    permission_classes = [permissions.AllowAny]
