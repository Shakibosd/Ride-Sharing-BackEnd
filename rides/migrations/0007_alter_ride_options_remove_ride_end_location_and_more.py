# Generated by Django 5.0.6 on 2024-08-30 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0006_remove_ride_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ride',
            options={'verbose_name_plural': 'Rider'},
        ),
        migrations.RemoveField(
            model_name='ride',
            name='end_location',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='name',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='start_location',
        ),
        migrations.AddField(
            model_name='ride',
            name='status',
            field=models.CharField(default='Pending', max_length=20),
        ),
        migrations.AddField(
            model_name='ride',
            name='where_ride_from',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ride',
            name='where_ride_to',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]