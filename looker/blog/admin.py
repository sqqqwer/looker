from django.contrib import admin

from models import PostLook, ClothesItem


class ClothesItemInLineAdmin(admin.TabularInline):
    model = ClothesItem


@admin.register(PostLook)
class PostLookAdmin(PostLook):
    inlines = [ClothesItemInLineAdmin]
