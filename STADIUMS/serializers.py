from rest_framework import serializers
from .models import Stadion, ManagerStadion, StadionImage
from django.contrib.auth import get_user_model

User = get_user_model()


class StadionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadionImage
        fields = ["id", "image", "uploaded_at"]


class StadionListSerializer(serializers.ModelSerializer):
    images = StadionImageSerializer(many=True, read_only=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = Stadion
        fields = [
            "id",
            "name",
            "slug",
            "location",
            "capacity",
            "status",
            "is_active",
            "images",
        ]


class StadionDetailSerializer(serializers.ModelSerializer):
    images = StadionImageSerializer(many=True, read_only=True)
    owner = serializers.StringRelatedField()

    class Meta:
        model = Stadion
        fields = "__all__"
        read_only_fields = ["slug", "created_at", "updated_at"]


class StadionCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stadion
        exclude = ["slug", "created_at", "updated_at"]


class ManagerStadionSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    stadion = serializers.StringRelatedField()

    class Meta:
        model = ManagerStadion
        fields = "__all__"


class ManagerStadionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerStadion
        fields = ["user", "stadion"]
