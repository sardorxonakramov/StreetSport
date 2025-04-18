from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Stadion, ManagerStadion
from .serializers import (
    StadionListSerializer,
    StadionDetailSerializer,
    StadionCreateUpdateSerializer,
    ManagerStadionSerializer,
    ManagerStadionCreateSerializer,
)
from .permissions import IsOwner
User = get_user_model()


# ✅ Admin — CRUD for all stadiums
class AdminStadionListCreateView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Stadion.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return StadionCreateUpdateSerializer
        return StadionListSerializer


class AdminStadionDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    queryset = Stadion.objects.all()
    serializer_class = StadionDetailSerializer

    def perform_update(self, serializer):
        serializer.save(is_active=True)


# ✅ Owner — view only their own stadiums
class OwnerStadionListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    serializer_class = StadionListSerializer

    def get_queryset(self):
        return Stadion.objects.filter(owner=self.request.user)


# ✅ Owner — create stadium
# owner is activ bermaydi faqat admin qila oladi.
class OwnerStadionCreateView(generics.CreateAPIView):
    permission_classes = [IsOwner, permissions.IsAuthenticated]
    serializer_class = StadionCreateUpdateSerializer

    def perform_create(self, serializer):
        if self.request.user.role == 'owner':
            serializer.save(owner=self.request.user, is_active=False)
        else:
            raise permissions.PermissionDenied('Siz owner emassiz!\nShuning uchun stadion kirita olmaysiz \nKiritish uchun adminga bog\'laning')


# ✅ Owner — update/delete only their own stadium
class OwnerStadionDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StadionDetailSerializer

    def get_queryset(self):
        return Stadion.objects.filter(owner=self.request.user)


# ✅ Owner — assign manager to a stadium
class AssignManagerView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ManagerStadionCreateSerializer

    def perform_create(self, serializer):
        stadion = serializer.validated_data["stadion"]
        if stadion.owner != self.request.user:
            raise permissions.PermissionDenied(
                "Siz bu stadionga manager biriktira olmaysiz."
            )
        serializer.save()


# ✅ Manager — view assigned stadiums
# meneger tamir va ochiq yoki yopiqligini boshqara oladi va 2 ta band qo'shish kerak
# band va bron qilingan qilish
class ManagerAssignedStadionListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = StadionListSerializer

    def get_queryset(self):
        manager_stadions = ManagerStadion.objects.filter(
            user=self.request.user, approved_by_owner=True
        )
        return Stadion.objects.filter(
            id__in=manager_stadions.values_list("stadion_id", flat=True)
        )


# buu yerga bron qilingan va band stadionlarni ko'rish mumkin
class OwnerDashboardView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        stadions = Stadion.objects.filter(owner=request.user)
        data = {
            "total_stadions": stadions.count(),
            "active_stadions": stadions.filter(is_active=True).count(),
            "inactive_stadions": stadions.filter(is_active=False).count(),
        }
        return Response(data)
