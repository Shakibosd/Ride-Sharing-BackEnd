# Generated by Django 5.0.6 on 2024-08-28 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0006_alter_driver_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
    ]
