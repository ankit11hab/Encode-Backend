# Generated by Django 3.2.7 on 2022-01-21 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0007_alter_testpayment_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='testpayment',
            name='verified',
            field=models.BooleanField(default=False),
        ),
    ]
