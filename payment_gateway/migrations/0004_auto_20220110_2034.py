# Generated by Django 3.2.7 on 2022-01-10 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_gateway', '0003_alter_testpayment_payment_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testpayment',
            old_name='user',
            new_name='passenger',
        ),
        migrations.AddField(
            model_name='testpayment',
            name='busNumber',
            field=models.CharField(default='', max_length=100),
        ),
    ]
