from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers


class ClientViewSet(ModelViewSet):
    queryset = models.EBankClient.objects.all()
    serializer_class = serializers.EBankClientSerializer


class ValuteViewSet(ModelViewSet):
    queryset = models.EBankValute.objects.all()
    serializer_class = serializers.EBankValuteSerializer


class AccountViewSet(ModelViewSet):
    queryset = models.EBankAccount.objects.all()
    serializer_class = serializers.EBankAccountSerializer


class LoanViewSet(ModelViewSet):
    queryset = models.EBankLoan.objects.all()
    serializer_class = serializers.EBankLoanSerializer


class SalaryViewSet(ModelViewSet):
    queryset = models.EBankSalary.objects.all()
    serializer_class = serializers.EBankSalarySerializer


class OperationTypeViewSet(ModelViewSet):
    queryset = models.EBankOperationType.objects.all()
    serializer_class = serializers.EBankOperationTypeSerializer


class OperationViewSet(ModelViewSet):
    queryset = models.EBankOperation.objects.all()
    serializer_class = serializers.EBankOperationSerializer
