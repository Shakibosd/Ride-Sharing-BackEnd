# Generated by Django 5.0.6 on 2024-09-13 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0055_remove_riderequest_driver'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RideRequest',
        ),
    ]
