# Generated by Django 5.0.6 on 2024-09-06 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0017_remove_riderequest_where_ride_from_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='riderequest',
            name='where_ride_from',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='riderequest',
            name='where_ride_to',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
