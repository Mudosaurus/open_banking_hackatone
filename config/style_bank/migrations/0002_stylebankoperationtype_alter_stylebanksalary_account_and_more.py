# Generated by Django 5.1.3 on 2024-11-23 02:07

import bank_api.money_field
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('style_bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StyleBankOperationType',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'operation type',
                'verbose_name_plural': 'operation types',
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='stylebanksalary',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='style_bank.stylebankaccount'),
        ),
        migrations.CreateModel(
            name='StyleBankOperation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('state', models.IntegerField(choices=[(0, 'Created'), (1, 'In progress'), (2, 'Commited'), (3, 'Rolled')], default=0, editable=False)),
                ('sum', bank_api.money_field.MoneyField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='style_bank.stylebankaccount')),
                ('operation_type', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='style_bank.stylebankoperationtype')),
            ],
            options={
                'verbose_name': 'bank operation',
                'verbose_name_plural': 'bank operations',
                'ordering': ('date_time',),
                'abstract': False,
            },
        ),
    ]
