# Generated by Django 5.0.6 on 2024-09-12 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0032_alter_riderequest_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ride',
            old_name='username',
            new_name='driver',
        ),
        migrations.RemoveField(
            model_name='riderequest',
            name='username',
        ),
    ]
