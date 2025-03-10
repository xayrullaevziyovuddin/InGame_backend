from rest_framework import serializers
from .models import Comment
from products.models import Product  # Убедись, что импорт правильный


class CommentSerializer(serializers.ModelSerializer):
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),  # Важно! Проверяем существование товара
        write_only=True,
        source='product'  # Явно указываем, что это поле 'product'
    )
    author_name = serializers.CharField(read_only=True)  # Делаем read_only
    author_email = serializers.EmailField(read_only=True)  # Делаем read_only

    class Meta:
        model = Comment
        fields = [
            'id',
            'product_id',
            'author_name',
            'author_email',
            'text',
            'rating',
            'created_at',
            'is_approved',
        ]
        read_only_fields = ('created_at', 'is_approved')  # is_approved тоже read_only

    def create(self, validated_data):
        # Устанавливаем пользователя, если он аутентифицирован
        user = self.context['request'].user
        if user.is_authenticated:
            validated_data['author_name'] = user.username  # Или другое поле с именем
            validated_data['author_email'] = user.email  # Если есть email

        return super().create(validated_data)