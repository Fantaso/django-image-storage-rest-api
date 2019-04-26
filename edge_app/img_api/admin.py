from django.contrib import admin

# from .models import ImageModel, ImageOutputModel
# from .models import ImageModel, ImageOutputBboxModel, ImageOutputModel


# ######### ADMIN ImageModel #########
# @admin.register(ImageModel)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ('status', 'imagePath', 'imageId')
#     list_filter = ('created_at',)
#
#
# ######### ADMIN ImageOutputModel #########
# @admin.register(ImageOutputModel)
# class ImageOutputAdmin(admin.ModelAdmin):
#     list_display = ('probability', 'label', 'result')
#     # list_display = ('output_image', 'probability', 'label', 'result', 'bbox')
#     list_filter = ('created_at',)


######### ADMIN ImageOutputBboxModel #########
# @admin.register(ImageOutputBboxModel)
# class ImageOutputBboxAdmin(admin.ModelAdmin):
#     list_display = ('output_bbox',)
#     list_filter = ('created_at',)
