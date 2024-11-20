from hob_api.models import *

APP_LABEL = 'style_bank'


class StyleBankClient(Client):
    class Meta:
        app_label = APP_LABEL


class StyleBankValute(Valute):
    class Meta:
        app_label = APP_LABEL


class StyleBankAccount(Account):
    class Meta:
        app_label = APP_LABEL


class StyleBankLoan(Loan):
    class Meta:
        app_label = APP_LABEL


class StyleBankSalary(Salary):
    class Meta:
        app_label = APP_LABEL
