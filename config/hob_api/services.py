from django.contrib import admin

from rest_framework import routers, permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from . import models
from . import views


class DBRouter(object):
    route_app_labels = {}
    db_name = str()

    def db_for_read(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return self.db_name
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label in self.route_app_labels \
            or obj2._meta.app_label in self.route_app_labels:
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label in self.route_app_labels:
            return db == self.db_name
        return None


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
            title="BlackCubics / Сервис согласий",
            description="Open Baning Api (team87)",
            default_version='v1',
        ),
        public=True,
        permission_classes=[permissions.AllowAny,],
    )
