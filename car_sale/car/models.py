from django.db import models
from django.urls import reverse


class Car(models.Model):
    brand = models.CharField(max_length=255, verbose_name='марка автомобиля')
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="url"
        )
    model = models.CharField(max_length=255, verbose_name='модель автомобиля')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='время создания'
        )
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True, verbose_name='публикация')
    date = models.IntegerField(
        null=True, verbose_name='год выпуска автомобиля'
        )
    price = models.IntegerField(null=True, verbose_name='цена автомобиля')
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
    cat = models.ForeignKey('Category_car', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('car:detail_car', kwargs={'car_slug': self.slug})

    def __str__(self):
        return self.brand
    
    class Meta:
        verbose_name = 'Машина'
        verbose_name_plural = 'Машины'
        ordering = ('-time_create', 'id')


class Category_car(models.Model):
    name = models.CharField(max_length=255, verbose_name='тип автомобиля')
    slug = models.SlugField(
        max_length=255, unique=True, db_index=True, verbose_name="url"
        )

    def get_absolute_url(self):
        return reverse('car:category', kwargs={'cat_slug': self.slug})

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория машин'
        verbose_name_plural = 'Категории машин'
        
