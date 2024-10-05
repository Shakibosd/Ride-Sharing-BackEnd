# Generated by Django 5.0.6 on 2024-08-29 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0011_alter_driver_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='driver',
            name='image',
        ),
        migrations.AddField(
            model_name='driver',
            name='par_hours',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=11),
            preserve_default=False,
        ),
    ]