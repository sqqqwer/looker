from rest_framework import serializers

from outfits.models import Outfit, ClothesItem


class OutfitSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
    )
    clothes = serializers.HyperlinkedRelatedField(
        view_name='clothesitem-detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Outfit
        fields = ('id', 'title', 'clothes', 'author', 'publication_date',
                  'image', 'description', 'created_at')
        read_only_fields = ('publication_date', )


class ClothesItemSerializer(serializers.ModelSerializer):
    outfit = serializers.HyperlinkedRelatedField(
        view_name='outfit-detail',
        read_only=True
    )

    class Meta:
        model = ClothesItem
        fields = ('title', 'outfit', 'url', 'image_url', 'cost')
        read_only_fields = ('image_url', 'cost')
