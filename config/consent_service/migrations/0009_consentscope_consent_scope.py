# Generated by Django 5.1.3 on 2024-11-22 20:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consent_service', '0008_rename_code_operationtype_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConsentScope',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'consent scope',
                'verbose_name_plural': 'consent scopes',
            },
        ),
        migrations.AddField(
            model_name='consent',
            name='scope',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='consent_service.consentscope'),
            preserve_default=False,
        ),
    ]
