# Generated by Django 3.1.7 on 2021-03-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='num_pages',
            field=models.IntegerField(default=0, verbose_name='Количество страниц'),
        ),
    ]
