# Generated by Django 5.0.2 on 2024-03-06 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_payment_orderplaced'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]