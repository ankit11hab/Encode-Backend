# Generated by Django 3.2.7 on 2022-01-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0004_auto_20220121_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='busroute',
            name='place_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
