# Generated by Django 5.0.6 on 2024-09-06 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0013_ride_created_by_riderequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='created_by',
        ),
    ]