# Generated by Django 5.1.3 on 2024-11-22 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consent_service', '0010_agent_consent_agent_client_alter_consentscope_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='api_address',
            field=models.URLField(null=True),
        ),
    ]