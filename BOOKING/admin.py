from django.contrib import admin
from .models import StadionBooking


@admin.register(StadionBooking)
class StadionBookingAdmin(admin.ModelAdmin):
    list_display = ('stadion', 'user', 'is_offline', 'is_active', 'booking_time')
    list_filter = ('is_offline', 'is_active', 'booking_time')
    search_fields = ('stadion__name', 'user__email')