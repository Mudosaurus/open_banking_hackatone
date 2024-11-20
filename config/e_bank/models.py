from hob_api.models import *

APP_LABEL = 'e_bank'


EBankClient(Client):
    class Meta:
        app_label = APP_LABEL


EBankValute(Valute):
    class Meta:
        app_label = APP_LABEL


EBankAccount(Account):
    class Meta:
        app_label = APP_LABEL


EBankLoan(Loan):
    class Meta:
        app_label = APP_LABEL


EBankSalary(Salary):
    class Meta:
        app_label = APP_LABEL
