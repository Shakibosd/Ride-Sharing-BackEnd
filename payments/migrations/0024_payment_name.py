# Generated by Django 5.0.6 on 2024-09-05 05:44

import drivers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0023_remove_payment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='name',
            field=models.CharField(default=1, max_length=50, verbose_name=drivers.models.Driver),
            preserve_default=False,
        ),
    ]