from django.db import models


class ImageModel(models.Model):
    PROCESSING = 'Processing'
    COMPLETE = 'Complete'
    STATUS_CHOICES = ((PROCESSING, 'Processing'), (COMPLETE, 'Complete'))

    status = models.CharField(max_length=10, blank=False, choices=STATUS_CHOICES)
    imagePath = models.CharField(max_length=200, blank=False)
    imageId = models.CharField(max_length=200, blank=False, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<imageId: {self.imageId}>'

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'image'
        verbose_name_plural = 'images'


class ImageOutputModel(models.Model):
    image = models.ForeignKey(ImageModel,
                              related_name='output', on_delete=models.CASCADE)

    probability = models.FloatField(blank=False)
    label = models.CharField(max_length=50, blank=False)
    result = models.CharField(max_length=50, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<output: {self.probability} {self.label} {self.result}>'

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'imageoutput'
        verbose_name_plural = 'imageoutputs'


class ImageOutputBboxModel(models.Model):
    image_output = models.ForeignKey(
        ImageOutputModel, related_name='bbox', on_delete=models.CASCADE)

    bbox_value = models.FloatField(blank=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'<bbox_value: {self.bbox_value}>'

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'imageoutputbbox'
        verbose_name_plural = 'imageoutputbboxs'
