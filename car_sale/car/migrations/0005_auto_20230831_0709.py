# Generated by Django 2.2.16 on 2023-08-31 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_auto_20230831_0708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='brand',
            field=models.CharField(max_length=255, verbose_name='марка автомобиля'),
        ),
    ]
