# Generated by Django 3.2.7 on 2022-01-22 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drivers', '0005_busroute_place_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='busroute',
            name='expected_time',
            field=models.TimeField(),
        ),
    ]
