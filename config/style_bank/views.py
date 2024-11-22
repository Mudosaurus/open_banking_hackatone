from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers


class ClientViewSet(ModelViewSet):
    queryset = models.StyleBankClient.objects.all()
    serializer_class = serializers.StyleBankClientSerializer


class ValuteViewSet(ModelViewSet):
    queryset = models.StyleBankValute.objects.all()
    serializer_class = serializers.StyleBankValuteSerializer


class AccountViewSet(ModelViewSet):
    queryset = models.StyleBankAccount.objects.all()
    serializer_class = serializers.StyleBankAccountSerializer


class LoanViewSet(ModelViewSet):
    queryset = models.StyleBankLoan.objects.all()
    serializer_class = serializers.StyleBankLoanSerializer


class SalaryViewSet(ModelViewSet):
    queryset = models.StyleBankSalary.objects.all()
    serializer_class = serializers.StyleBankSalarySerializer
