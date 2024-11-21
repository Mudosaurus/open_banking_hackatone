from django.db import models
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


class OperationType(models.Model):
    code = models.CharField(primary_key=True, max_length=6, blank=False)
    description = models.TextField(blank=False, null=False)
    
    def __str__(self):
        return f'operation type {self.code} - {self.description}'

    class Meta:
        verbose_name = 'operation type'
        verbose_name_plural = 'operation types'


class OperationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OperationType
        fields = ('code', 'description')
        