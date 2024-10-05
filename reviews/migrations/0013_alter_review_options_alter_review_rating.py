# Generated by Django 5.0.6 on 2024-09-05 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0012_alter_review_options_alter_review_rating'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name_plural': 'Review'},
        ),
        migrations.AlterField(
            model_name='review',
            name='rating',
            field=models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=5),
        ),
    ]
