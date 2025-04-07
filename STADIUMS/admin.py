from django.contrib import admin
from .models import Stadion, ManagerStadion, StadionImage


@admin.register(Stadion)
class StadionAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'location', 'capacity', 'status', 'is_active')
    list_filter = ('status', 'is_active', 'location')
    search_fields = ('name', 'location')
    autocomplete_fields = ['owner']  # bu bilan katta ro'yxatdan tez izlash mumkin


@admin.register(ManagerStadion)
class ManagerStadionAdmin(admin.ModelAdmin):
    list_display = ('user', 'stadion', 'approved_by_owner', 'assigned_at')
    list_filter = ('approved_by_owner',)
    autocomplete_fields = ['user', 'stadion']  # userda limit_choices_to ishlaydi


@admin.register(StadionImage)
class StadionImageAdmin(admin.ModelAdmin):
    list_display = ('stadion', 'image', 'uploaded_at')
