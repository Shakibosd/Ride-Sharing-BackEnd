# Generated by Django 5.0.6 on 2024-09-05 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0027_payment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='name',
        ),
    ]
