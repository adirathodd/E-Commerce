# Generated by Django 4.2 on 2023-06-03 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_alter_bid_bid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='bid',
            new_name='bid2',
        ),
    ]
