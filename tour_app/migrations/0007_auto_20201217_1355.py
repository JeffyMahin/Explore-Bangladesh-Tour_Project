# Generated by Django 3.1.2 on 2020-12-17 07:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tour_app', '0006_auto_20201217_1329'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('police_station', models.CharField(max_length=255)),
                ('police_phone', models.CharField(max_length=25)),
                ('fire_service', models.CharField(max_length=255)),
                ('fire_phone', models.CharField(max_length=25)),
            ],
        ),
        migrations.AlterField(
            model_name='location',
            name='created_at',
            field=models.TimeField(default=datetime.datetime(2020, 12, 17, 13, 55, 53, 489736)),
        ),
    ]