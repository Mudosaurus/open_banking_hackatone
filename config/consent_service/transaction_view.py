from rest_framework.viewsets import ModelViewSet
from .transaction_model import Transaction, TransactionSerializer


class TransactionViewSet(ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    