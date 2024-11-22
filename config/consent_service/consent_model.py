import uuid
# from django.contrib.postgres.fields import ArrayField
from django.db import models
from rest_framework import serializers
from .transaction_model import Transaction


class Consent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    expire_date_time = models.DateTimeField()
    expire_transaction = models.ForeignKey(Transaction, on_delete=models.DO_NOTHING, null=True)
    agent = models.UUIDField(blank=False, null=False)
    contragent = models.UUIDField(blank=False, null=False)
    agreement = models.BooleanField(default=False, null=False)

    def __str__(self):
        return f'consent from {self.agent} to {self.contragent} with expire date {self.expire_date_time} is {self.agreement}'

    class Meta:
        verbose_name = 'consent'
        verbose_name_plural = 'consents'
        

class ConsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consent
        fields = ('id', 'expire_date_time', 'expire_transaction', 'agent', 'contragent', 'agreement')
