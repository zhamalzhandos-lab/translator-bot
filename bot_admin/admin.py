from django.contrib import admin
from .models import UserQuery

@admin.register(UserQuery)
class UserQueryAdmin(admin.ModelAdmin):
    list_display = ("username", "telegram_id", "word", "translation", "found", "created_at")
    list_filter = ("found", "created_at")
    search_fields = ("username", "word", "telegram_id")
    readonly_fields = ("created_at",)
