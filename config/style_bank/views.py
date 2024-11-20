from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class ClientViewSet(ModelViewSet):
    queryset = models.StyleBankClient.objects.all()
    serializer_class = serializers.ClientSerializer


class ValuteViewSet(ModelViewSet):
    queryset = models.StyleBankValute.objects.all()
    serializer_class = serializers.ValuteSerializer


class AccountViewSet(ModelViewSet):
    queryset = models.StyleBankAccount.objects.all()
    serializer_class = serializers.AccountSerializer


class LoanViewSet(ModelViewSet):
    queryset = models.StyleBankLoan.objects.all()
    serializer_class = serializers.LoanSerializer


class SalaryViewSet(ModelViewSet):
    queryset = models.StyleBankSalary.objects.all()
    serializer_class = serializers.SalarySerializer
