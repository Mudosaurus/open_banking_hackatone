from rest_framework import serializers

from . import models


class EBankClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EBankClient
        fields = ('id', 'first_name', 'last_name', 'family_name')


class EBankValuteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EBankValute
        fields = ('id', 'code', 'name')


class EBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EBankAccount
        fields = ('id', 'holder', 'valute', 'balance')


class EBankLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EBankLoan
        fields = ('id', 'borrower', 'credit_sum', 'pay_rest', 'monthly_pay', 'get_date', 'repayment_date', 'documents')


class EBankSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.EBankSalary
        fields = ('id', 'account', 'date_time', 'sum', 'category', 'type')
