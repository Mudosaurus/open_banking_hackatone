import requests
from django.db import models
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from .transaction_model import Transaction
from .agent_model import Agent
from .operation_type_model import ConsentOperattionType


class AtomicOperation(models.Model):
    class State(models.IntegerChoices):
        CREATED = 0, _("Created")
        IN_PROGRESS = 1, _("In progress")
        COMMITED = 2, _("Commited")
        ROLLED = 3, _("Rolled")
        
    transaction = models.ForeignKey(Transaction, null=False, blank=False, on_delete=models.RESTRICT)
    operation_type = models.ForeignKey(ConsentOperattionType, null=False, blank=False, on_delete=models.RESTRICT)    
    state = models.IntegerField(choices=State, default=State.CREATED, null=False, editable=False)
    last_state_date_time = models.DateTimeField(blank=False, null=False, editable=False, auto_now=True)
    agent = models.ForeignKey(Agent, blank=False, null=False, on_delete=models.RESTRICT, related_name='%(class)s_agent')
    contragent = models.ForeignKey(Agent, on_delete=models.RESTRICT, null=True, blank=True, related_name='%(class)s_contragent')
    agent_details = models.JSONField(null=True, blank=True)
    contragent_details = models.JSONField(null=True, blank=True)
    
    def __str__(self):
        return f'atomic operation {self.operation_type} in {self.transaction} in state {self.state}'

    class Meta:
        verbose_name = 'atomic operation'
        verbose_name_plural = 'atomic operations'
        order_with_respect_to = 'transaction'
                                
    def start(self):
        # if self.state != self.State.CREATED:
        #     raise ValueError(f'{str(self)} is not in CREATE state')
        
        self.state = self.State.IN_PROGRESS
        self.save()                        
        
        self.__call_agent_api(self.agent, self.agent_details)
        
        if self.contragent:
            self.__call_agent_api(self.contragent, self.contragent_details)
            
        self.state = self.State.COMMITED
        self.save()                                    
            
    def __call_agent_api(self, agent, operation_details):
        if not agent.api_address:
            raise ValueError(f'No api address for {str(agent)}')
        
        headers = {'operation-type': self.operation_type.id}
        
        if operation_details:
            headers['operation-details'] = str(operation_details)
                    
        response = requests.post(agent.api_address + '/execute_operation', headers=headers)
        
        if not response.ok:
            raise RuntimeError(f'{response.status_code} - {response.content}')
            

class AtomicOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtomicOperation
        fields = ('id', 'transaction', '_order', 'state', 'last_state_date_time', 'operation_type', 'agent', 'contragent', 'agent_details', 'contragent_details')
        