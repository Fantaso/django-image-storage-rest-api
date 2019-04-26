# from django.utils import timezone

from rest_framework import serializers

# from .models import ImageModel, ImageOutputModel
from .models import ImageModel, ImageOutputBboxModel, ImageOutputModel


class ImageOutputBboxSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = ImageOutputBboxModel
        fields = ('bbox_value',)
        # read_only_fields = ('id', 'created_at', 'updated_at')


class ImageOutputSerializer(serializers.ModelSerializer):
    bbox = ImageOutputBboxSerializer(many=True)

    class Meta:
        lookup_field = 'id'
        model = ImageOutputModel
        fields = ('probability', 'label', 'result', 'bbox')


class ImageSerializer(serializers.ModelSerializer):
    output = ImageOutputSerializer(many=True)

    class Meta:
        lookup_field = 'id'
        model = ImageModel
        fields = ('status', 'imagePath', 'imageId', 'output')
        # read_only_fields = ('id', 'created_at', 'updated_at')
        # depth = 2

    def create(self, validated_data):
        output_data = validated_data.pop('output')
        image = ImageModel.objects.create(**validated_data)
        for output in output_data:
            ImageOutputModel.objects.create(image=image, **output)
        return image


# IMPORTS
# from img_api.models import *
# from img_api.serializers import *
# TEST SERIALIZER
# s = ImageSerializer()
# print(repr(s))
'''
ImageSerializer():
    status = ChoiceField(choices=(('Processing', 'Processing'), ('Complete', 'Complete')))
    imagePath = CharField(label='ImagePath', max_length=200)
    imageId = CharField(label='ImageId', max_length=200, validators=[ < UniqueValidator(queryset=ImageModel.objects.all()) > ])
    output = ImageOutputSerializer(many=True):
        image = PrimaryKeyRelatedField(queryset=ImageModel.objects.all())
        probability = FloatField()
        label = CharField(max_length=50)
        result = CharField(max_length=50)
'''
# TEST SERILIZER CREATTION
# from img_api.serializers import *
# from img_api.models import *
# image1 = ImageModel.objects.create(status=ImageModel.COMPLETE, imagePath="1", imageId="1")
# output1 = ImageOutputModel.objects.create(image=image1, probability=1, label="1", result="1")
# bbox1 = ImageOutputBboxModel.objects.create(image_output=output1, bbox_value=100)

# TEST SERIALIZER DATA
data = {
    "status": "Complete",
    "imagePath": "7",
    "imageId": "7",
    "output": [
        {
            "probability": 7.0,
            "label": "7",
            "result": "7"
        }
    ]
}

data2 = {
    "status": "Complete",
    "imagePath": "2",
    "imageId": "2",
    "output": [
        {
            "probability": 2.0,
            "label": "2",
            "result": "2"
        }
    ]
}


# from img_api.serializers import *
# from img_api.models import *
# serializer = ImageSerializer(data=data2)
# serializer.is_valid()
# serializer.save()
