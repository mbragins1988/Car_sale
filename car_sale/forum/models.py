from django.db import models


class Forum(models.Model):
    title = models.CharField(max_length=255, verbose_name='название поста')
    text = models.TextField(max_length=2000, verbose_name='текс поста')
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name='фото автомобиля',
        blank=True,
    )

    def __str__(self):
        return self.title
