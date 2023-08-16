# Generated by Django 3.2.20 on 2023-08-11 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='data',
            field=models.DateTimeField(blank=True, max_length=50, verbose_name='дата выпуска автомобиля'),
        ),
        migrations.AlterField(
            model_name='car',
            name='number_owners',
            field=models.IntegerField(blank=True, verbose_name='количество владельцев'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(blank=True, verbose_name='цена автомобиля'),
        ),
    ]
