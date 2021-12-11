# Generated by Django 3.2.9 on 2021-11-30 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_bid_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='winlist',
            field=models.ManyToManyField(blank=True, related_name='userWinListings', to='market.AuctionListing'),
        ),
    ]
