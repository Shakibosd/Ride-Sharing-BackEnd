# Generated by Django 5.0.6 on 2024-09-12 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0030_ride_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='user',
            new_name='username',
        ),
        migrations.RenameField(
            model_name='riderequest',
            old_name='user',
            new_name='username',
        ),
    ]
