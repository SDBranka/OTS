# Generated by Django 2.2 on 2021-07-05 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imgfield_app', '0003_product_manufacturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='office_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='special_instructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='office_notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='special_instructions',
            field=models.TextField(blank=True, null=True),
        ),
    ]
