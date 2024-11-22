from django.db import models
from rest_framework import serializers


class OperationType(models.Model):
    id = models.CharField(primary_key=True, max_length=6, blank=False)
    description = models.TextField(blank=False, null=False)
    
    def __str__(self):
        return f'operation type {self.id} - {self.description}'

    class Meta:
        verbose_name = 'operation type'
        verbose_name_plural = 'operation types'


class OperationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationType
        fields = ('id', 'description')
        