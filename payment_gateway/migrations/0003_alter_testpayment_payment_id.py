# Generated by Django 3.2.7 on 2021-12-31 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0002_auto_20211231_1138'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testpayment',
            name='payment_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
