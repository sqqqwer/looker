from rest_framework import viewsets
from django.contrib.auth import get_user_model

from outfits.models import Outfit, ClothesItem
from api.serializers import (
    OutfitSerializer,
    ClothesItemSerializer
)


User = get_user_model()


class OutfitViewSet(viewsets.ModelViewSet):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer

    def perform_create(self, serializer):
        serializer.save(author=User.objects.get(id=1))


class ClothesItemViewSet(viewsets.ModelViewSet):
    queryset = ClothesItem.objects.all()
    serializer_class = ClothesItemSerializer

    def perform_create(self, serializer):
        serializer.save(outfit=Outfit.objects.get(id=1))
