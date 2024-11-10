from django.contrib import admin

from rest_framework import routers, permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import models
from . import views


def register_api_to_admin():
    admin.site.register(models.Client, admin.ModelAdmin)
    admin.site.register(models.Valute, admin.ModelAdmin)
    admin.site.register(models.Account, admin.ModelAdmin)
    admin.site.register(models.Loan, admin.ModelAdmin)
    admin.site.register(models.Salary, admin.ModelAdmin)


def get_router() -> routers.DefaultRouter:
    router = routers.DefaultRouter()
    router.register(r'clients', views.ClientViewSet)
    router.register(r'valutes', views.ValuteViewSet)
    router.register(r'accounts', views.AccountViewSet)
    router.register(r'loans', views.LoanViewSet)
    router.register(r'salaries', views.SalaryViewSet)
    return router


def get_swagger_schema_view() -> type:
    return get_schema_view(
        openapi.Info(
            title="TheSocial",
            description="TheSocial (team87) Open Baning Api",
            default_version='v1',
        ),
        public=True,
        permission_classes=[permissions.AllowAny, ],
    )
