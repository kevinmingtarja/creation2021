# Generated by Django 3.1.2 on 2020-12-17 03:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statement_1',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 3, 55, 33, 524474, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statement_2',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 3, 55, 33, 524960, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='statement_3',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 12, 17, 3, 55, 33, 525411, tzinfo=utc)),
        ),
    ]
