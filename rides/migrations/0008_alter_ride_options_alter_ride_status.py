# Generated by Django 5.0.6 on 2024-08-30 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0007_alter_ride_options_remove_ride_end_location_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ride',
            options={'verbose_name_plural': 'Rides'},
        ),
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed')], default='Pending', max_length=20),
        ),
    ]
