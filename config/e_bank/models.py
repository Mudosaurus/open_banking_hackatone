from hob_api.models import *

app_label = 'e_bank'

Client.Meta.app_label = app_label
Valute.Meta.app_label = app_label
Account.Meta.app_label = app_label
Loan.Meta.app_label = app_label
Salary.Meta.app_label = app_label
