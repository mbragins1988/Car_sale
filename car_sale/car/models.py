from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=255, verbose_name='марка автомобиля')
    model = models.CharField(max_length=255, verbose_name='модель автомобиля')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    date = models.IntegerField(
        max_length=50, null=True,
        verbose_name='год выпуска автомобиля'
    )
    price = models.IntegerField(
        null=True, verbose_name='цена автомобиля'
    )
    number_owners = models.IntegerField(
        null=True, blank=True, verbose_name='количество владельцев'
    )
    text = models.TextField(
        null=True, blank=True, verbose_name='описание автомобиля'
    )
    photo = models.ImageField(
        upload_to="photos/%Y/%m/%d/", verbose_name='фото автомобиля',
        blank=True,
    )

    def __str__(self):
        return self.brand
