# Generated by Django 5.0.6 on 2024-07-03 16:24

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_is_sale_product_sale_price_alter_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='star',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 7, 3, 20, 54, 18, 549193)),
        ),
    ]
