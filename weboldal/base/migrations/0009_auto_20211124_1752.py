# Generated by Django 3.2.8 on 2021-11-24 16:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20211124_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolygo',
            name='leiras',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='haz',
            name='leiras',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='jegy',
            name='leiras',
            field=models.TextField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='horoszkop1',
            name='idopont',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 24, 17, 52, 2, 519324)),
        ),
    ]
