# Generated by Django 5.0.6 on 2024-09-12 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0019_alter_riderequest_driver'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RideRequest',
        ),
    ]
