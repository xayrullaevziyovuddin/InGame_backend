from rest_framework import serializers
from .models import AttributeType, Attribute


class AttributeTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AttributeType
        fields = ["id", "name"]


class AttributeSerializer(serializers.ModelSerializer):
    attribute_type = AttributeTypeSerializer(read_only=True)  # В ответе будет объект
    attribute_type_id = serializers.PrimaryKeyRelatedField(
        queryset=AttributeType.objects.all(), source="attribute_type", write_only=True
    )  # При создании можно передавать ID

    class Meta:
        model = Attribute
        fields = ["id", "attribute_type", "attribute_type_id", "value"]

