# Generated by Django 5.0.6 on 2024-08-29 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0018_alter_driver_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='image',
            field=models.ImageField(upload_to='drivers/images/'),
        ),
    ]
