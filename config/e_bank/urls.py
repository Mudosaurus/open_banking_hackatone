from django.urls import path, include
from rest_framework import routers
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
    path('', include(get_router().urls))
]
