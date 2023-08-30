from django.db import models
from django.urls import reverse


class Forum(models.Model):
    title = models.CharField(max_length=255, verbose_name='название поста')
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="url"
        )
    text = models.TextField(max_length=2000, verbose_name='текс поста')
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name='фото автомобиля',
        blank=True,
    )
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category_forum', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('forum:post_detail', kwargs={'post_slug': self.slug})
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Форум'
        verbose_name_plural = 'Форум'


class Category_forum(models.Model):
    name = models.CharField(
        max_length=100, db_index=True, verbose_name='название темы'
    )
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="url"
        )

    def get_absolute_url(self):
        return reverse('forum:category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория форума'
        verbose_name_plural = 'Категории форума'
