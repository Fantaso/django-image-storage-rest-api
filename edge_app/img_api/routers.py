from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from .views import ImageViewSet, ImageOuputViewSet


######### NESTING ROUTER EXTENSION CLASS #########
class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass


######### NESTING ROUTER OBJECT #########
image_api_router = NestedDefaultRouter()


######### REGISTER ROUTER ImageViewSet #########
image_router = image_api_router.register('images', ImageViewSet)
image_router.register('output',
                      ImageOuputViewSet,
                      base_name='image-output',
                      parents_query_lookups=['image'],
                      )
# parents_query_lookups= ImageOutputModel.objects.filter(image={image})


######### REGISTER ROUTER ImageOuputViewSet #########
image_api_router.register('imageoutputs', ImageOuputViewSet)
