from rest_framework import serializers
from .models import StadionBooking


class StadionBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = StadionBooking
        fields = '__all__'
        read_only_fields = ['user', 'is_offline', 'booking_time']
