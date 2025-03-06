from rest_framework import viewsets
from .models import AttributeType, Attribute
from .serializers import AttributeTypeSerializer, AttributeSerializer


class AttributeTypeViewSet(viewsets.ModelViewSet):
    queryset = AttributeType.objects.all()
    serializer_class = AttributeTypeSerializer


class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer


