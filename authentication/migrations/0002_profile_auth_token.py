# Generated by Django 3.2.7 on 2022-01-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='auth_token',
            field=models.CharField(default='', max_length=100),
        ),
    ]
