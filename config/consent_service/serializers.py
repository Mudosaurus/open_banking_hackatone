from rest_framework import serializers

from . import models


class ConsentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Consent
        fields = ('id', 'zone', 'organizations', 'agreement')
