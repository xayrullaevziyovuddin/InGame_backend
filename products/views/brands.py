from rest_framework import viewsets
from ..models import Brand
from ..serializers import BannerSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BannerSerializer



