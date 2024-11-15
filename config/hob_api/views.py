from rest_framework.viewsets import ModelViewSet

from . import serializers
from . import models


class ClientViewSet(ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.ClientSerializer
    
    
class ValuteViewSet(ModelViewSet):
    queryset = models.Valute.objects.all()
    serializer_class = serializers.ValuteSerializer
    
  
class AccountViewSet(ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = serializers.AccountSerializer
    
    
class LoanViewSet(ModelViewSet):
    queryset = models.Loan.objects.all()
    serializer_class = serializers.LoanSerializer


class SalaryViewSet(ModelViewSet):
    queryset = models.Salary.objects.all()
    serializer_class = serializers.SalarySerializer
