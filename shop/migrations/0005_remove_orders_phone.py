# Generated by Django 3.0.8 on 2020-07-15 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='phone',
        ),
    ]
