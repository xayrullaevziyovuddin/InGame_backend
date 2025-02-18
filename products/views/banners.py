from rest_framework import viewsets
from django.http import JsonResponse
from products.models import Banner
from products.serializers import BannerSerializer


class BannerViewSet(viewsets.ModelViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

    def retrieve(self, request, *args, **kwargs):
        banner = Banner.objects.get(pk=kwargs['pk'])
        serializer = self.get_serializer(banner)
        return JsonResponse(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = BannerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.data, status=400)



