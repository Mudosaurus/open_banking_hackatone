from rest_framework.viewsets import ModelViewSet
from .operation_type_model import OperationType, OperationTypeSerializer


class OperationTypeViewSet(ModelViewSet):
    queryset = OperationType.objects.all()
    serializer_class = OperationTypeSerializer
