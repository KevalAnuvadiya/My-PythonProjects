# Generated by Django 4.1.5 on 2023-01-06 03:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 1, 6, 3, 42, 48, 396600, tzinfo=datetime.timezone.utc)),
        ),
    ]