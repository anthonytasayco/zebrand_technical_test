# Generated by Django 3.2 on 2023-07-03 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='times_visited',
            field=models.PositiveIntegerField(default=0, verbose_name='times visited'),
        ),
    ]