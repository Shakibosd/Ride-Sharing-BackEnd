# Generated by Django 5.0.6 on 2024-09-02 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0015_payment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='name',
        ),
    ]
