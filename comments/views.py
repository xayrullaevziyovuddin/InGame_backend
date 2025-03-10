from rest_framework import viewsets, permissions, status
from .models import Comment
from .serializers import CommentSerializer
from rest_framework.response import Response
from products.models import Product  # Проверь импорт

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        # Фильтрация по product_id (показывать комментарии только к конкретному товару)
        product_id = self.request.query_params.get('product_id')
        queryset = Comment.objects.all()
        if product_id is not None:
            queryset = queryset.filter(product_id=product_id)
        return queryset


    def get_permissions(self):
        # Разные права доступа для разных действий
        if self.action == 'create':
             # Создавать могут все (и анонимы тоже)
            permission_classes = [permissions.AllowAny]
        elif self.action in ['update', 'partial_update', 'destroy']:
            # Редактировать/удалять - только админы
            permission_classes = [permissions.IsAdminUser]
        else:
            # Остальные действия (list, retrieve) - всем
            permission_classes = [permissions.AllowAny]  # Или IsAuthenticated, если хочешь
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # Проверка на аутентификацию и заполнение author_name/email
        if not request.user.is_authenticated and (not serializer.validated_data.get('author_name') or not serializer.validated_data.get('author_email')):
            return Response({'error': 'Необходимо указать имя и email для неаутентифицированных пользователей.'}, status=status.HTTP_400_BAD_REQUEST)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)