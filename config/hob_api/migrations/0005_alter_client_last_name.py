# Generated by Django 5.1.3 on 2024-11-10 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hob_api', '0004_valute_alter_client_options_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
