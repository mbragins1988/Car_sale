# Generated by Django 3.2.20 on 2023-08-11 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_auto_20230811_0634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='data',
            field=models.DateTimeField(blank=True, max_length=50, null=True, verbose_name='дата выпуска автомобиля'),
        ),
        migrations.AlterField(
            model_name='car',
            name='number_owners',
            field=models.IntegerField(blank=True, null=True, verbose_name='количество владельцев'),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='цена автомобиля'),
        ),
    ]
