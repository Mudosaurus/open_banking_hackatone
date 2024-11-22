import uuid
from django.db import models
from rest_framework import serializers
        
        
class Agent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False)
    api_address = models.URLField(null=True)
    
    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'agent'
        verbose_name_plural = 'agents'


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('id', 'name', 'api_address')
