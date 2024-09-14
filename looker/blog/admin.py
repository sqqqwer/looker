from django.contrib import admin

from .models import Outfit, ClothesItem


class ClothesItemInLineAdmin(admin.TabularInline):
    model = ClothesItem


@admin.register(Outfit)
class OutfitAdmin(admin.ModelAdmin):
    inlines = [ClothesItemInLineAdmin]
