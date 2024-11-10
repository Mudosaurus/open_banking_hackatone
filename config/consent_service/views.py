from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers

class ConsentViewSet(ModelViewSet):
    queryset = models.Consent.objects.all()
    serializer_class = serializers.ConsentSerializer
