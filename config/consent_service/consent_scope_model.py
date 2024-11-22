from django.db import models
from rest_framework import serializers


class ConsentScope(models.Model):
    id = models.CharField(primary_key=True, max_length=6, blank=False)
    description = models.TextField(blank=False, null=False)
    
    def __str__(self):
        return f'consent scope {self.id} - {self.description}'
    
    class Meta:
        verbose_name = 'consent scope'
        verbose_name_plural = 'consent scopes'


class ConsentScopeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsentScope
        fields = ('id', 'description')
