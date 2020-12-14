# Generated by Django 3.1.2 on 2020-12-14 08:02

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('img', models.ImageField(upload_to='img')),
                ('img_url', models.CharField(blank=True, max_length=300)),
                ('raw', models.FileField(upload_to='img')),
                ('raw_url', models.CharField(blank=True, max_length=300)),
                ('time', models.DateTimeField(default=datetime.datetime(2020, 12, 14, 8, 2, 26, 10257, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
