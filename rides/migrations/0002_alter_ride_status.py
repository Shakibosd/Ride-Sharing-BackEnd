# Generated by Django 5.0.6 on 2024-08-26 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Complete', 'Complete')], default='Pending', max_length=50),
        ),
    ]
