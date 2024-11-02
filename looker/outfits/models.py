from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


OUTFIT_TITLE_MAX_LENGTH = 256

CLOTHESITEM_TITLE_MAX_LENGTH = 100

STR_OUTPUT_LIMIT = 20

User = get_user_model()


class Outfit(models.Model):
    created_at = models.DateTimeField('Добавлено', auto_now_add=True)
    is_published = models.BooleanField('Опубликовано', default=True)

    publication_date = models.DateTimeField('Дата и время публикации',
                                            null=True,
                                            default=None)
    image = models.ImageField('Изображение',
                              upload_to='postlook_image',
                              blank=True)
    title = models.CharField('Название',
                             max_length=OUTFIT_TITLE_MAX_LENGTH)
    description = models.TextField('Описание',
                                   blank=True)

    author = models.ForeignKey(User,
                               on_delete=models.CASCADE,
                               verbose_name='Автор публикации')

    class Meta:
        verbose_name = 'публикация образа'
        verbose_name_plural = 'Публикации образов'
        default_related_name = 'outfit'

        # ordering = ('-publication_date',)

    def __str__(self):
        return self.title[:STR_OUTPUT_LIMIT]


class ClothesItem(models.Model):
    title = models.CharField('Название',
                             max_length=CLOTHESITEM_TITLE_MAX_LENGTH)
    url = models.URLField('Ссылка')
    image_url = models.URLField('Ссылка на изображение',
                                null=True, default=None)

    outfit = models.ForeignKey(Outfit,
                               on_delete=models.CASCADE,
                               verbose_name='Одежда образа')
    cost = models.PositiveIntegerField('Цена', default=10)
    order_number = models.PositiveSmallIntegerField(default=10)

    class Meta:
        verbose_name = 'одежда образа'
        verbose_name_plural = 'Одежда образов'
        default_related_name = 'clothes'

        ordering = ('order_number',)

    def get_absolute_url(self):
        return reverse('parent-detail', kwargs={'clothes_id': str(self.pk)})

    def __str__(self):
        return self.title[:STR_OUTPUT_LIMIT]
