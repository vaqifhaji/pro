from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import User, BlockedIpAddress

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'first_name', 'last_name', 'phone', 'is_staff', 'date_joined']
    search_fields = ['email', 'first_name', 'last_name', 'phone']
    list_filter = ['is_staff', 'is_active', 'date_joined']
    ordering = ['-date_joined']

@admin.register(BlockedIpAddress)
class BlockedIpAddressAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'reason', 'blocked_at']
    search_fields = ['ip_address']
    list_filter = ['blocked_at']
