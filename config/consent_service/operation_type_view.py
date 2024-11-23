from rest_framework.viewsets import ModelViewSet
from .operation_type_model import ConsentOperattionType, ConsentOperationTypeSerializer


class ConsentOperationTypeViewSet(ModelViewSet):
    queryset = ConsentOperattionType.objects.all()
    serializer_class = ConsentOperationTypeSerializer

