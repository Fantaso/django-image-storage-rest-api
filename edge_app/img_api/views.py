from rest_framework import viewsets

from .models import ImageModel, ImageOutputModel
# from .models import ImageModel, ImageOutputBboxModel, ImageOutputModel

from.serializers import ImageSerializer, ImageOutputSerializer
# from.serializers import ImageSerializer, ImageOutputSerializer, ImageOutputBboxSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = ImageModel.objects.all()
    serializer_class = ImageSerializer


class ImageOuputViewSet(viewsets.ModelViewSet):
    queryset = ImageOutputModel.objects.all()
    serializer_class = ImageOutputSerializer


# class ImageOutputBboxViewSet(viewsets.ModelViewSet):
#     queryset = ImageOutputBboxModel.objects.all()
#     serializer_class = ImageOutputBboxSerializer
