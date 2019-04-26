from django.urls import include, path

from .routers import image_api_router

urlpatterns = [
    path('', include(image_api_router.urls)),
]
