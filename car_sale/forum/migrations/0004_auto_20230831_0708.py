# Generated by Django 2.2.16 on 2023-08-31 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20230830_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='фото'),
        ),
    ]