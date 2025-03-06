# Файл: comments/serializers.py
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев"""

    class Meta:
        model = Comment
        fields = [
            "id", "product", "author_name", "author_email",
            "text", "rating", "created_at"
        ]
        extra_kwargs = {
            "author_email": {"write_only": True},  # Email не будет возвращаться в API
        }


# Файл: comments/views.py
from rest_framework import viewsets, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """API для работы с комментариями"""
    queryset = Comment.objects.filter(is_approved=True)
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ["product", "rating"]
    ordering_fields = ["created_at", "rating"]
    ordering = ["-created_at"]

    def get_permissions(self):
        """
        Разрешения для разных методов:
        - Создавать комментарии может любой
        - Изменять и удалять только администратор
        """
        if self.action in ["create", "list", "retrieve"]:
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        """При создании комментария он не одобрен по умолчанию"""
        serializer.save(is_approved=False)


# Файл: comments/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CommentViewSet

router = DefaultRouter()
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

# Добавьте в config/urls.py:
# path("api/", include("comments.urls")),