# Generated by Django 3.2 on 2021-04-26 08:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('beam_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='scooters',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
