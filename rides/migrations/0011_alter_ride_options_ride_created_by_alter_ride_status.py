# Generated by Django 5.0.6 on 2024-09-05 19:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0010_delete_orderhistory'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ride',
            options={},
        ),
        migrations.AddField(
            model_name='ride',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Ride Completed', 'Ride Completed')], default='Pending', max_length=20),
        ),
    ]
