# Generated by Django 3.2.7 on 2021-12-31 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payment_gateway', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testpayment',
            name='name',
        ),
        migrations.AddField(
            model_name='testpayment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
