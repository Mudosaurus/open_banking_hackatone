from django.db import models
from bank_api.models import Client, Valute, Account, Loan, Salary

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
    account = models.ForeignKey(StyleBankAccount, on_delete=models.DO_NOTHING, null=False)
    
    class Meta(Salary.Meta):
        app_label = APP_LABEL
