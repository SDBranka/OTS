# Generated by Django 2.2 on 2021-07-09 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgfield_app', '0019_auto_20210709_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='placed_at',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 9, 7, 10, 35, 127303)),
        ),
    ]