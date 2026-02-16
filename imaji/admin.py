from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import User, Post


# -------------------------------
# User Admin
# -------------------------------
@admin.register(User)
class UserAdmin(ModelAdmin):
    list_display = ("username", "email", "is_staff", "is_active", "date_joined")
    list_filter = ("is_staff", "is_active", "date_joined")
    search_fields = ("username", "email")
    ordering = ("-date_joined",)

    fieldsets = (
        ("Authentication", {"fields": ("username", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )


# -------------------------------
# Post Admin
# -------------------------------
@admin.register(Post)
class PostAdmin(ModelAdmin):
    list_display = ("title", "author", "status", "created_at", "updated_at")
    list_filter = ("status", "created_at", "author", "tags")  # filter by tags
    search_fields = ("title", "content", "author__username", "tags__name")
    ordering = ("-created_at",)
    prepopulated_fields = {"slug": ("title",)}  #  auto-fill slug from title

    fieldsets = (
        (
            "Content",
            {"fields": ("title", "slug", "content", "image", "tags")},
        ),  # added tags here
        ("Meta", {"fields": ("author", "status")}),
        ("Timestamps", {"fields": ("created_at", "updated_at")}),
    )

    readonly_fields = ("created_at", "updated_at")
