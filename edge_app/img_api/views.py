from rest_framework import viewsets

from .models import ImageModel, ImageOutputModel


from.serializers import ImageSerializer, ImageOutputSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer


class ImageOuputViewSet(viewsets.ModelViewSet):
    queryset = ImageOutputModel.objects.all()
    serializer_class = ImageOutputSerializer
