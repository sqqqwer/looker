# Generated by Django 5.1.1 on 2024-10-20 01:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Outfit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Добавлено')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('publication_date', models.DateTimeField(blank=True, verbose_name='Дата и время публикации')),
                ('image', models.ImageField(blank=True, upload_to='postlook_image', verbose_name='Изображение')),
                ('title', models.CharField(max_length=256, verbose_name='Название')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор публикации')),
            ],
            options={
                'verbose_name': 'публикация образа',
                'verbose_name_plural': 'Публикации образов',
                'default_related_name': 'outfit',
            },
        ),
        migrations.CreateModel(
            name='ClothesItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('url', models.URLField(verbose_name='Ссылка')),
                ('image_url', models.URLField(default=None, null=True, verbose_name='Ссылка на изображение')),
                ('cost', models.PositiveIntegerField(default=10, verbose_name='Цена')),
                ('order_number', models.PositiveSmallIntegerField(default=10)),
                ('outfit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outfits.outfit', verbose_name='Одежда образа')),
            ],
            options={
                'verbose_name': 'одежда образа',
                'verbose_name_plural': 'Одежда образов',
                'ordering': ('order_number',),
                'default_related_name': 'clothes',
            },
        ),
    ]
