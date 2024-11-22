from django.db import models
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .transaction_model import Transaction
from .operation_type_model import OperationType


class AtomicOperation(models.Model):
    class State(models.IntegerChoices):
        CREATED = 0, _("Created")
        IN_PROGRESS = 1, _("In progress")
        COMMITED = 2, _("Commited")
        ROLLED = 3, _("Rolled")
        
    transaction = models.ForeignKey(Transaction, null=False, blank=False, on_delete=models.RESTRICT)
    state = models.IntegerField(choices=State, default=State.CREATED, null=False, editable=False)
    last_state_date_time = models.DateTimeField(blank=False, null=False, editable=False, auto_now=True)
    operation_type = models.ForeignKey(OperationType, null=False, on_delete=models.RESTRICT)
    agent = models.UUIDField(blank=False, null=False)
    contragent = models.UUIDField()
    details = models.JSONField()
    
    def __str__(self):
        return f'atomic operation {self.operation_type.code} in transaction {self.transaction} in state {self.state}, details: {self.details}'

    class Meta:
        verbose_name = 'atomic operation'
        verbose_name_plural = 'atomic operations'
        order_with_respect_to = 'transaction'


class AtomicOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtomicOperation
        fields = ('id', 'transaction', '_order', 'state', 'last_state_date_time', 'operation_type', 'agent', 'contragent', 'details')
        