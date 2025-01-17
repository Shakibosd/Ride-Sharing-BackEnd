# Generated by Django 5.0.6 on 2024-09-04 07:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0022_rename_where_ride_to_where_ride_driver_where_ride_from_and_more'),
        ('payments', '0019_payment_driver_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='driver_info',
        ),
        migrations.AlterField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drivers.driver'),
        ),
    ]
