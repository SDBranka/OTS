# Generated by Django 2.2 on 2021-07-06 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('imgfield_app', '0008_auto_20210706_0021'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_1', models.CharField(max_length=54)),
                ('address_2', models.CharField(max_length=54)),
                ('city', models.CharField(max_length=54)),
                ('state', models.CharField(max_length=54)),
                ('country', models.CharField(max_length=54)),
                ('phone', models.CharField(max_length=14)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='order_contact_info', to='imgfield_app.Order')),
                ('quote', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quote_contact_info', to='imgfield_app.Quote')),
                ('user', models.ManyToManyField(related_name='user_contact_infos', to='imgfield_app.User')),
            ],
        ),
    ]