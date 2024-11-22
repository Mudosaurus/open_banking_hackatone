import uuid
from datetime import datetime, timedelta
from django.db import models
from rest_framework import serializers


class Transaction(models.Model):
    def default_date_time():
        return datetime.now() + timedelta(days=1)
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_time = models.DateTimeField(blank=False, null=False, editable=False, auto_now_add=True)
    expire_date_time = models.DateTimeField(blank=False, null=False, editable=True, default=default_date_time)
    
    def __str__(self):
        return f'Transaction {self.id} from {self.date_time}'

    class Meta:
        verbose_name = 'transaction'
        verbose_name_plural = 'transactions'
        

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'date_time', 'expire_date_time')
        