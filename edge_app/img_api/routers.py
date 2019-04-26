from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from .views import ImageViewSet, ImageOuputViewSet
# from .views import ImageOuputViewSet, ImageOutputBboxViewSet, ImageViewSet


######### NESTING ROUTER EXTENSION CLASS #########
class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


######### NESTING ROUTER OBJECT #########
image_api_router = NestedDefaultRouter()


######### REGISTER ROUTER ImageViewSet #########
image_api_router.register('images', ImageViewSet)


######### REGISTER ROUTER ImageOuputViewSet #########
image_api_router.register('imageoutputs', ImageOuputViewSet)


######### REGISTER ROUTER ImageOutputBboxViewSet #########
# image_api_router.register('imageoutputbboxs', ImageOutputBboxViewSet)
