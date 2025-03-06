# Файл: comments/admin.py
from django.contrib import admin
from .models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "author_name", "rating", "created_at", "is_approved")
    list_filter = ("is_approved", "rating", "created_at")
    search_fields = ("author_name", "author_email", "text")
    list_editable = ("is_approved",)
    readonly_fields = ("created_at",)
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        """Групповое одобрение комментариев"""
        queryset.update(is_approved=True)
        self.message_user(request, f"Одобрено {queryset.count()} комментариев")

    approve_comments.short_description = "Одобрить выбранные комментарии"