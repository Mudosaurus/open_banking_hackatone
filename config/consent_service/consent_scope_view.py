from rest_framework.viewsets import ModelViewSet
from .consent_scope_model import ConsentScope, ConsentScopeSerializer


class ConsentScopeViewSet(ModelViewSet):
    queryset = ConsentScope.objects.all()
    serializer_class = ConsentScopeSerializer
    