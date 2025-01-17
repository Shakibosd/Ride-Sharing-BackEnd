# Generated by Django 5.0.6 on 2024-09-05 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0022_rename_where_ride_to_where_ride_driver_where_ride_from_and_more'),
        ('payments', '0050_remove_payment_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='driver',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='drivers.driver'),
            preserve_default=False,
        ),
    ]
