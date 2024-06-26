# Generated by Django 5.0.2 on 2024-03-11 15:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_supplier_delete_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='product',
            name='selling_price',
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.supplier'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('punjab', 'Punjab'), ('kpk', 'KPK'), ('sindh', 'Sindh'), ('balochistan', 'Balochistan'), ('G-B', 'G-B')], max_length=100),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='payment',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='app.payment'),
        ),
        migrations.AlterField(
            model_name='orderplaced',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Pending', 'Pending')], default='Pending', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='product',
            name='discounted_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='products'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='address',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='contact_number',
            field=models.CharField(max_length=20),
        ),
    ]
