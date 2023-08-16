from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=255, verbose_name='марка автомобиля')
    model = models.CharField(max_length=255, verbose_name='модель автомобиля')
    date = models.DateTimeField(
        max_length=50, null=True, blank=True,
        verbose_name='год выпуска автомобиля'
    )
    price = models.IntegerField(
        null=True, blank=True, verbose_name='цена автомобиля'
    )
    number_owners = models.IntegerField(
        null=True, blank=True, verbose_name='количество владельцев'
    )
    text = models.TextField(
        null=True, blank=True, verbose_name='описание автомобиля'
    )
    photo = models.ImageField(
        null=True, blank=True, verbose_name='фото автомобиля'
    )

    def __str__(self):
        return self.brand
