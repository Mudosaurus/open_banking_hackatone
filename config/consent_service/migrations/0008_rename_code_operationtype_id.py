# Generated by Django 5.1.3 on 2024-11-22 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consent_service', '0007_alter_transaction_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operationtype',
            old_name='code',
            new_name='id',
        ),
    ]
