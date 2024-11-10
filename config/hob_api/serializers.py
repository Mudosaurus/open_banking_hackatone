from . import models
from rest_framework import serializers


class TestModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TestModel
        fields = ('id', 'name',)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ('id', 'first_name', 'last_name', 'family_name')
        
        
class ValuteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Valute
        fields = ('id', 'code', 'name')
        
                
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = ('id', 'holder', 'valute', 'balance')


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Loan
        fields = ('id', 'borrower', 'credit_sum', 'pay_rest', 'monthly_pay', 'get_date', 'repayment_date', 'documents')


class SalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Salary
        fields = ('id', 'account', 'date_time', 'sum', 'category', 'type')
