# Generated by Django 5.0.6 on 2024-09-12 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0035_rename_user_ride_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='username',
            new_name='user',
        ),
    ]
