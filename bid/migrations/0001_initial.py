# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bidding_Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bid_price', models.DecimalField(max_digits=60, decimal_places=2)),
                ('bidding_date', models.CharField(max_length=20)),
                ('is_Exit', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Item_Info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=255)),
                ('item_type', models.CharField(max_length=255)),
                ('item_info', models.CharField(max_length=255)),
                ('item_img_path', models.ImageField(upload_to=b'item')),
                ('item_location', models.CharField(max_length=255)),
                ('item_destination', models.CharField(max_length=255)),
                ('bid_start_time', models.CharField(max_length=20)),
                ('bid_close_time', models.CharField(max_length=20)),
                ('bid_start_price', models.DecimalField(max_digits=60, decimal_places=2)),
                ('is_confirm', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Transporter_Info',
            fields=[
                ('user_name', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('owner_name', models.CharField(max_length=255)),
                ('Mobile_no', models.CharField(max_length=13, blank=True)),
                ('email_id', models.CharField(max_length=255, blank=True)),
                ('transport_name', models.CharField(max_length=255)),
                ('registration_number', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('user_name', models.CharField(max_length=255, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=13, blank=True)),
                ('email_id', models.CharField(max_length=255, blank=True)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='item_info',
            name='user_id',
            field=models.ForeignKey(to='bid.User_Info'),
        ),
        migrations.AddField(
            model_name='bidding_info',
            name='bid_person_id',
            field=models.ForeignKey(to='bid.Transporter_Info'),
        ),
        migrations.AddField(
            model_name='bidding_info',
            name='item_id',
            field=models.ForeignKey(to='bid.Item_Info'),
        ),
    ]
