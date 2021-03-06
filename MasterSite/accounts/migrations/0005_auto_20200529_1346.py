# Generated by Django 3.0.3 on 2020-05-29 12:46

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200517_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='account',
            name='profile_pic',
            field=models.ImageField(default='accounts/default/default.png', upload_to=accounts.models.upload_location),
        ),
    ]
