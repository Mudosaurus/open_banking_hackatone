from django.urls import path, include
from rest_framework import routers
from bank_api.execute_operation import execute_operation
from .models import StyleBankOperation, StyleBankOperationType, StyleBankAccount
from . import views


def get_router() -> routers.DefaultRouter:
    router = routers.DefaultRouter()
    router.register(r'clients', views.ClientViewSet)
    router.register(r'valutes', views.ValuteViewSet)
    router.register(r'accounts', views.AccountViewSet)
    router.register(r'loans', views.LoanViewSet)
    router.register(r'salaries', views.SalaryViewSet)
    router.register(r'operation_types', views.OperationTypeViewSet)
    router.register(r'operations', views.OperationViewSet)    
    
    
    return router

urlpatterns = [
    path('api/execute_operation',
         execute_operation,
         name='execute_operation',
         kwargs={'operation_model': StyleBankOperation, 'operation_type_model': StyleBankOperationType, 'account_model': StyleBankAccount}),
    path('', include(get_router().urls))
]
