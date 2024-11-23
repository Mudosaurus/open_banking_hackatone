from django.db import models
from bank_api.models import Client, Valute, Account, Loan, Salary, OperationType, Operation

APP_LABEL = 'style_bank'


class StyleBankClient(Client):
    class Meta(Client.Meta):
        app_label = APP_LABEL


class StyleBankValute(Valute):
    class Meta(Valute.Meta):
        app_label = APP_LABEL


class StyleBankAccount(Account):
    holder = models.ForeignKey(StyleBankClient, on_delete=models.DO_NOTHING, blank=False, null=False)
    valute = models.ForeignKey(StyleBankValute, on_delete=models.DO_NOTHING, blank=False)    
    class Meta(Account.Meta):
        app_label = APP_LABEL


class StyleBankLoan(Loan):
    borrower = models.ForeignKey(StyleBankClient, on_delete=models.DO_NOTHING, blank=False, null=False)    
    
    class Meta(Loan.Meta):
        app_label = APP_LABEL


class StyleBankSalary(Salary):
    account = models.ForeignKey(StyleBankAccount, on_delete=models.RESTRICT, null=False, blank=False)
    
    class Meta(Salary.Meta):
        app_label = APP_LABEL


class StyleBankOperationType(OperationType):
    class Meta(OperationType.Meta):
        app_label = APP_LABEL


class StyleBankOperation(Operation):
    operation_type = models.ForeignKey(StyleBankOperationType, null=False, blank=False, on_delete=models.RESTRICT)    
    account = models.ForeignKey(StyleBankAccount, on_delete=models.RESTRICT, null=False, blank=False)    

    class Meta(Operation.Meta):
        app_label = APP_LABEL
        