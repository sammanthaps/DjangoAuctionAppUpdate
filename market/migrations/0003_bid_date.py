# Generated by Django 3.2.9 on 2021-11-30 21:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0002_auctionlisting_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 30, 21, 5, 17, 255368, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
