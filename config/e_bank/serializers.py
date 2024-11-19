from hob_api.serializers import *
from . import models

ClientSerializer.Meta.model = models.Client
ValuteSerializer.Meta.model = models.Valute
AccountSerializer.Meta.model = models.Account
LoanSerializer.Meta.model = models.Loan
SalarySerializer.Meta.model = models.Salary
