# Generated by Django 5.0.6 on 2024-09-12 21:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0023_alter_driver_options'),
        ('rides', '0052_alter_ride_driver'),
    ]

    operations = [
        migrations.AddField(
            model_name='riderequest',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='rides', to='drivers.driver'),
        ),
        migrations.AlterField(
            model_name='ride',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='drivers.driver'),
        ),
    ]