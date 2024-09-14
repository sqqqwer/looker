from django.contrib.auth import get_user_model
from django.db import models


OUTFIT_TITLE_MAX_LENGTH = 256
OUTFIT_STR_OUTPUT_LIMIT = 10

CLOTHESITEM_TITLE_MAX_LENGTH = 100
CLOTHESITEM_STR_OUTPUT_LIMIT = 10

User = get_user_model()


class Outfit(models.Model):
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
    publication_date = models.DateTimeField('Дата и время публикации')
    is_published = models.BooleanField('Опубликовано', default=True)

    image = models.ImageField('Изображение',
                              upload_to='postlook_image',
                              blank=True)
    title = models.CharField('Название',
                             max_length=OUTFIT_TITLE_MAX_LENGTH)
    description = models.TextField('Описание')

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор публикации')

    class Meta:
        verbose_name = 'публикация образа'
        verbose_name_plural = 'Публикации образов'
        default_related_name = 'postlooks'

        ordering = ('-publication_date',)

    def __str__(self):
        return self.title[:OUTFIT_STR_OUTPUT_LIMIT]


class ClothesItem(models.Models):
    title = models.CharField('Название',
                             max_length=CLOTHESITEM_TITLE_MAX_LENGTH,
                             on_delete=models.CASCADE,
                             verbose_name='Одежда образа')

    postlook = models.ForeignKey()

    order_number = models.PositiveSmallIntegerField(default=10)

    class Meta:
        verbose_name = 'одежда образа'
        verbose_name_plural = 'Одежда образов'
        default_related_name = 'clothes'

        ordering = ('order_number',)

    def __str__(self):
        return self.title[:CLOTHESITEM_STR_OUTPUT_LIMIT]
