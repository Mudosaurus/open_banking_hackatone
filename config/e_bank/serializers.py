from bank_api.serializers import ClientSerializer, ValuteSerializer, AccountSerializer, LoanSerializer, SalarySerializer, OperationTypeSerializer, OperationSerializer
from . import models


class EBankClientSerializer(ClientSerializer):
    class Meta(ClientSerializer.Meta):
        model = models.EBankClient


class EBankValuteSerializer(ValuteSerializer):
    class Meta(ValuteSerializer.Meta):
        model = models.EBankValute


class EBankAccountSerializer(AccountSerializer):
    class Meta(AccountSerializer.Meta):
        model = models.EBankAccount


class EBankLoanSerializer(LoanSerializer):
    class Meta(LoanSerializer.Meta):
        model = models.EBankLoan


class EBankSalarySerializer(SalarySerializer):
    class Meta(SalarySerializer.Meta):
        model = models.EBankSalary


class EBankOperationTypeSerializer(OperationTypeSerializer):
    class Meta(OperationTypeSerializer.Meta):
        model = models.EBankOperationType


class EBankOperationSerializer(OperationSerializer):
    class Meta(OperationSerializer.Meta):
        model = models.EBankOperation
