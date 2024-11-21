from rest_framework.viewsets import ModelViewSet

from .consent_model import Consent, ConsentSerializer

class ConsentViewSet(ModelViewSet):
    queryset = Consent.objects.all()
    serializer_class = ConsentSerializer
