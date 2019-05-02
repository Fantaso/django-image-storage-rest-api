# from django.utils import timezone

from rest_framework import serializers

from .models import ImageModel, ImageOutputModel


class ImageOutputSerializer(serializers.ModelSerializer):

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

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.content = validated_data.get('content', instance.content)
    #     instance.created = validated_data.get('created', instance.created)
    #     instance.save()
    #     return instance
