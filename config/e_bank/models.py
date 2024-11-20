from hob_api.models import *

APP_LABEL = 'e_bank'


class EBankClient(Client):
    class Meta:
        app_label = APP_LABEL


class EBankValute(Valute):
    class Meta:
        app_label = APP_LABEL


class EBankAccount(Account):
    class Meta:
        app_label = APP_LABEL


class EBankLoan(Loan):
    class Meta:
        app_label = APP_LABEL


class EBankSalary(Salary):
    class Meta:
        app_label = APP_LABEL
