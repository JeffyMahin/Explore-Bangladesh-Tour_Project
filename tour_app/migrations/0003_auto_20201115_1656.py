# Generated by Django 3.1.3 on 2020-11-15 10:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_app', '0002_auto_20201115_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='division',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='guidedetails',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2020, 11, 15, 16, 56, 20, 745949)),
        ),
        migrations.AlterField(
            model_name='location',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
