# Generated by Django 5.0.6 on 2024-09-02 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0010_payment_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='user',
            new_name='username',
        ),
    ]
