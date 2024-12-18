# Generated by Django 5.1.3 on 2024-11-22 21:47

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consent_service', '0009_consentscope_consent_scope'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'agent',
                'verbose_name_plural': 'agents',
            },
        ),
        migrations.AddField(
            model_name='consent',
            name='agent_client',
            field=models.UUIDField(default='b356c912-8024-40f5-a562-2a7861371596'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='consentscope',
            name='id',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='atomicoperation',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='%(class)s_agent', to='consent_service.agent'),
        ),
        migrations.AlterField(
            model_name='atomicoperation',
            name='contragent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='%(class)s_contragent', to='consent_service.agent'),
        ),
        migrations.AlterField(
            model_name='consent',
            name='agent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='%(class)s_agent', to='consent_service.agent'),
        ),
        migrations.AlterField(
            model_name='consent',
            name='contragent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='%(class)s_contragent', to='consent_service.agent'),
        ),
    ]
