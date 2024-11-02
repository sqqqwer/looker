from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (
    OutfitViewSet,
    ClothesItemViewSet
)


v1_router = DefaultRouter()
v1_router.register('outfits', OutfitViewSet, basename='outfit')
v1_router.register('clothes', ClothesItemViewSet, basename='clothesitem')

urlpatterns = [
    path('v1/', include(v1_router.urls))
]
