# Generated by Django 3.0.3 on 2020-03-09 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20200308_2004'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Watchlist',
        ),
    ]