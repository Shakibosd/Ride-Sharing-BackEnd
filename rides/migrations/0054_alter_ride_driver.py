# Generated by Django 5.0.6 on 2024-09-12 21:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0023_alter_driver_options'),
        ('rides', '0053_riderequest_driver_alter_ride_driver'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ride', to='drivers.driver'),
        ),
    ]
