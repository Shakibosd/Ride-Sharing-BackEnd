# Generated by Django 5.0.6 on 2024-08-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0012_remove_driver_image_driver_par_hours'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='driving_licence',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='driver',
            name='number_plate',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]