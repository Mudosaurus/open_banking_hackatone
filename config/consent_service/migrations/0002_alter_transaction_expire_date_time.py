# Generated by Django 5.1.3 on 2024-11-22 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consent_service', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='expire_date_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 11, 23, 9, 30, 45, 138562)),
        ),
    ]