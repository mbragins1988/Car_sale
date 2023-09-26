# Generated by Django 2.2.16 on 2023-08-28 11:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='тип автомобиля')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=255, verbose_name='марка автомобиля')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='url')),
                ('model', models.CharField(max_length=255, verbose_name='модель автомобиля')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
                ('date', models.IntegerField(null=True, verbose_name='год выпуска автомобиля')),
                ('price', models.IntegerField(null=True, verbose_name='цена автомобиля')),
                ('number_owners', models.IntegerField(blank=True, null=True, verbose_name='количество владельцев')),
                ('text', models.TextField(blank=True, null=True, verbose_name='описание автомобиля')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото автомобиля')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='car.Category_car')),
            ],
        ),
    ]
