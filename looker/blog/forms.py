from django.forms import ModelForm, DateTimeInput

from .models import Outfit, ClothesItem


class OutfitForm(ModelForm):
    class Meta:
        model = Outfit
        exclude = ('created_at', 'is_published', 'author')
        widgets = {
            'publication_date': DateTimeInput(
                format='%Y-%m-%dT%H:%M:%S',
                attrs={'type': 'datetime-local'}
            )
        }


class ClothesItemForm(ModelForm):
    class Meta:
        model = ClothesItem
        fields = ('title', 'url')
