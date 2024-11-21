from rest_framework import serializers

from . import models


class StyleBankClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StyleBankClient
        fields = ('id', 'first_name', 'last_name', 'family_name')


class StyleBankValuteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StyleBankValute
        fields = ('code', 'name')


class StyleBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StyleBankAccount
        fields = ('id', 'holder', 'valute', 'balance')


class StyleBankLoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StyleBankLoan
        fields = ('id', 'borrower', 'credit_sum', 'pay_rest', 'monthly_pay', 'get_date', 'repayment_date', 'documents')


class StyleBankSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StyleBankSalary
        fields = ('id', 'account', 'date_time', 'sum', 'category', 'type')
