# Generated by Django 5.0.2 on 2024-03-11 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_product_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='discounted_price',
            new_name='price',
        ),
    ]