# Generated by Django 2.2 on 2021-07-08 23:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgfield_app', '0013_quote_placed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='placed_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 8, 19, 57, 51, 172778)),
        ),
        migrations.AlterField(
            model_name='quoteitem',
            name='combined_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='quoteproduct',
            name='combined_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]