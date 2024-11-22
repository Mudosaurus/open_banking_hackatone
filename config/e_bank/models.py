from django.db import models
from bank_api.models import Client, Valute, Account, Loan, Salary

APP_LABEL = 'e_bank'


class EBankClient(Client):
    class Meta(Client.Meta):
        app_label = APP_LABEL


class EBankValute(Valute):
    class Meta(Valute.Meta):
        app_label = APP_LABEL


class EBankAccount(Account):
    holder = models.ForeignKey(EBankClient, on_delete=models.DO_NOTHING, blank=False, null=False)
    valute = models.ForeignKey(EBankValute, on_delete=models.DO_NOTHING, blank=False)
    
    class Meta(Account.Meta):
        app_label = APP_LABEL


class EBankLoan(Loan):
    borrower = models.ForeignKey(EBankClient, on_delete=models.DO_NOTHING, blank=False, null=False)    
    
    class Meta(Loan.Meta):
        app_label = APP_LABEL


class EBankSalary(Salary):
    account = models.ForeignKey(EBankAccount, on_delete=models.DO_NOTHING, null=False)    
    
    class Meta(Salary.Meta):
        app_label = APP_LABEL
