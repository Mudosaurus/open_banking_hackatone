from bank_api.serializers import ClientSerializer, ValuteSerializer, AccountSerializer, LoanSerializer, SalarySerializer, OperationTypeSerializer, OperationSerializer
from . import models


class StyleBankClientSerializer(ClientSerializer):
    class Meta(ClientSerializer.Meta):
        model = models.StyleBankClient


class StyleBankValuteSerializer(ValuteSerializer):
    class Meta(ValuteSerializer.Meta):
        model = models.StyleBankValute


class StyleBankAccountSerializer(AccountSerializer):
    class Meta(AccountSerializer.Meta):
        model = models.StyleBankAccount


class StyleBankLoanSerializer(LoanSerializer):
    class Meta(LoanSerializer.Meta):
        model = models.StyleBankLoan


class StyleBankSalarySerializer(SalarySerializer):
    class Meta(SalarySerializer.Meta):
        model = models.StyleBankSalary


class StyleBankOperationTypeSerializer(OperationTypeSerializer):
    class Meta(OperationTypeSerializer.Meta):
        model = models.StyleBankOperationType


class StyleBankOperationSerializer(OperationSerializer):
    class Meta(OperationSerializer.Meta):
        model = models.StyleBankOperation
