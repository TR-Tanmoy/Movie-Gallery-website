# Generated by Django 3.1.3 on 2020-12-08 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_auto_20201208_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
