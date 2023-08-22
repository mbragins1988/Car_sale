from django.db import models
from django.urls import reverse


class Forum(models.Model):
    title = models.CharField(max_length=255, verbose_name='название поста')
    text = models.TextField(max_length=2000, verbose_name='текс поста')
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name='фото автомобиля',
        blank=True,
    )
    time_create = models.DateTimeField(auto_now_add=True, null=True)
    time_update = models.DateTimeField(auto_now=True, null=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category_forum', on_delete=models.PROTECT, null=True)
    
    def __str__(self):
        return self.title


class Category_forum(models.Model):
    name = models.CharField(
        max_length=100, db_index=True, verbose_name='тип автомобиля'
    )

    def get_absolute_url(self):
        return reverse('forum:category', kwargs={'cat_id': self.id})

    def __str__(self):
        return self.name
