# Generated by Django 3.2.7 on 2022-01-21 11:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0005_auto_20220110_2040'),
    ]

    operations = [
        migrations.AddField(
            model_name='testpayment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 21, 16, 40, 37, 828745)),
        ),
    ]