# Generated by Django 5.0.6 on 2024-08-28 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0003_alter_driver_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='driver',
            old_name='user',
            new_name='username',
        ),
    ]
