# Generated by Django 5.0.6 on 2024-09-05 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0036_alter_payment_driver_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='driver_name',
            field=models.CharField(max_length=50),
        ),
    ]
