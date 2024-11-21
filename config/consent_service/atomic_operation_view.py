from rest_framework.viewsets import ModelViewSet
from .atomic_operation_model import AtomicOperation, AtomicOperationSerializer


class AtomicOperationViewSet(ModelViewSet):
    queryset = AtomicOperation.objects.all()
    serializer_class = AtomicOperationSerializer
