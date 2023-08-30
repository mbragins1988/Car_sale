# Generated by Django 2.2.16 on 2023-08-30 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category_forum',
            options={'verbose_name': 'Категория форума', 'verbose_name_plural': 'Категории форума'},
        ),
        migrations.AlterModelOptions(
            name='forum',
            options={'verbose_name': 'Форум', 'verbose_name_plural': 'Форум'},
        ),
        migrations.RenameField(
            model_name='category_forum',
            old_name='slug',
            new_name='cat_slug',
        ),
        migrations.AlterField(
            model_name='category_forum',
            name='name',
            field=models.CharField(db_index=True, max_length=100, verbose_name='название темы'),
        ),
    ]
