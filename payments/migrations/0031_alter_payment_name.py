# Generated by Django 5.0.6 on 2024-09-05 05:57

import drivers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0030_alter_payment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='name',
            field=models.CharField(max_length=50, verbose_name=drivers.models.Driver),
        ),
    ]
