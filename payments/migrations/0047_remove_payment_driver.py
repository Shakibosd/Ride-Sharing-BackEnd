# Generated by Django 5.0.6 on 2024-09-05 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0046_alter_payment_driver'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='driver',
        ),
    ]
