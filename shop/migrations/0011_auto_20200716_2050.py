# Generated by Django 3.0.8 on 2020-07-16 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_orders_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='orders',
            name='phone',
            field=models.IntegerField(default=''),
        ),
    ]
