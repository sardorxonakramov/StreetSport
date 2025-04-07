from rest_framework import serializers
from .models import Stadion, ManagerStadion, StadionImage
from django.contrib.auth import get_user_model

User = get_user_model()


class StadionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadionImage
        fields = ["id", "image", "uploaded_at"]


class StadionSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()  # faqat email yoki __str__ ko‘rsatadi
    images = StadionImageSerializer(many=True, read_only=True)

    class Meta:
        model = Stadion
        fields = [
            "id",
            "name",
            "slug",
            "owner",
            "location",
            "capacity",
            "date_opened",
            "image",
            "description",
            "status",
            "is_active",
            "created_at",
            "updated_at",
            "images",
        ]
        read_only_fields = ["slug", "created_at", "updated_at"]


class StadionCreateSerializer(serializers.ModelSerializer):
    """
    Faqat admin yoki owner yangi stadion qo‘shishi uchun — owner ID yuboradi
    """

    class Meta:
        model = Stadion
        fields = [
            "name",
            "owner",
            "location",
            "capacity",
            "date_opened",
            "image",
            "description",
            "status",
            "is_active",
        ]


class ManagerStadionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    stadion = serializers.StringRelatedField()

    class Meta:
        model = ManagerStadion
        fields = ["id", "user", "stadion", "assigned_at", "approved_by_owner"]


class ManagerStadionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerStadion
        fields = ["user", "stadion"]
