# Generated by Django 5.0.6 on 2024-08-29 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0009_alter_driver_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
