from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class ClientViewSet(ModelViewSet):
    queryset = models.EBankClient.objects.all()
    serializer_class = serializers.ClientSerializer


class ValuteViewSet(ModelViewSet):
    queryset = models.EBankValute.objects.all()
    serializer_class = serializers.ValuteSerializer


class AccountViewSet(ModelViewSet):
    queryset = models.EBankAccount.objects.all()
    serializer_class = serializers.AccountSerializer


class LoanViewSet(ModelViewSet):
    queryset = models.EBankLoan.objects.all()
    serializer_class = serializers.LoanSerializer


class SalaryViewSet(ModelViewSet):
    queryset = models.EBankSalary.objects.all()
    serializer_class = serializers.SalarySerializer
