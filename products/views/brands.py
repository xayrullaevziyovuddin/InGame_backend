# Исправленный файл products/views/brands.py:
from rest_framework import viewsets
from ..models import Brand
from ..serializers import BrandSerializers


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializers